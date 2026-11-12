#ドメイン層
from abc import ABC, abstractmethod
from typing import Optional

#継承を用いている
#例外
class OrderError(Exception):
    pass

class OutOfStockError(OrderError):
    pass

class InsufficientBalanceError(OrderError):
    pass

class InvalidStateTransitionError(OrderError):
    pass


#ドメインイベント
class DomainEvent:
    pass

#注文が支払い済みであることを表すクラス
class OrderPaid(DomainEvent):
    def __init__(self, order_id, amount: int):
        self.order_id = order_id
        self.amount = amount


#ValueObject
class OrderId:
    def __init__(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("OrderId is invalid")
        self._value = value

    @property
    def value(self):
        return self._value

#__eq__()はインスタンスが==の引数として使用されたときに必ず呼ばれる関数（インスタンス以外のオブジェクトとの比較時は通らない）
    def __eq__(self, other):
        return isinstance(other, OrderId) and self.value == other.value

#pythonのクラス関数は通常仮想関数
#ABCを継承し、 @abstractmethodを使うことで、基底クラスをインスタンス化させないようにできる（インスタンス化すると、TypeErrorが発生する）
#Repository interface
class OrderRepository(ABC):
    @abstractmethod
    def get(self, order_id: OrderId):
        pass

    @abstractmethod
    def save(self, order):
        pass


class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id):
        pass

    @abstractmethod
    def save(self, user):
        pass


class ProductRepository(ABC):
    @abstractmethod
    def get(self, product_id):
        pass

    @abstractmethod
    def save(self, product):
        pass


#Entity
class Product:
    def __init__(self, product_id, price: int, stock: int):
        if price < 1:
            raise ValueError()
        if stock < 0:
            raise ValueError()

        self._id = product_id
        self._price = price
        self._stock = stock

    @property
    def id(self):
        return self._id
    
    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def decrease_stock(self):
        if self._stock == 0:
            raise OutOfStockError()
        self._stock -= 1

    def return_product(self):
        self._stock += 1


class User:
    def __init__(self, user_id, balance: int):
        if balance < 0:
            raise ValueError()

        self._id = user_id
        self._balance = balance

    @property
    def id(self):
        return self._id
    @property
    def balance(self):
        return self._balance

    def pay(self, amount: int):
        if self._balance < amount:
            raise InsufficientBalanceError()
        self._balance -= amount

    def refund(self, amount: int):
        self._balance += amount


class Coupon:
    def __init__(self, discount_amount: int):
        if discount_amount < 1:
            raise ValueError()
        self._discount_amount = discount_amount

    def apply(self, price):
        if self._discount_amount > price:
            raise ValueError()
        return price - self._discount_amount


# --- Order ---
from enum import Enum, auto

class OrderStatus(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELED = auto()

class OrderAction(Enum):
    PAY = auto()
    CANCEL = auto()
    SHIP = auto()

#ALLOWED_TRANSITIONSはキーの状態から、値の状態に遷移できるアクションを定義している
ALLOWED_TRANSITIONS = {
    OrderStatus.CREATED: {
        OrderAction.PAY: OrderStatus.PAID,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.PAID: {
        OrderAction.SHIP: OrderStatus.SHIPPED,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.SHIPPED: {},
    OrderStatus.CANCELED: {},
}


class Order:
    def __init__(self, 
        order_id, 
        user_id, 
        product_id, 
        status: OrderStatus = OrderStatus.CREATED, 
        paid_amount: int = 0, 
        coupon: Optional[Coupon] = None
    ):
        self._id = order_id
        self._user_id = user_id
        self._product_id = product_id
        self._coupon = coupon
        self._status = status
        self._events = []
        self._paid_amount = paid_amount

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def events(self):
        return list(self._events)

    @property
    def status(self):
        return self._status

    @property
    def paid_amount(self):
        return self._paid_amount

    def clear_events(self):
        self._events.clear()

    def calculate_price(self, base_price):
        if self._coupon:
            return self._coupon.apply(base_price)
        return base_price

    #状態の遷移
    def _transition(self, action):
        if action not in ALLOWED_TRANSITIONS[self._status]:
            raise InvalidStateTransitionError()
        self._status = ALLOWED_TRANSITIONS[self._status][action]

    def mark_as_paid(self, amount):
        self._paid_amount = amount
        self._transition(OrderAction.PAY)
        #eventsにOrderPaidイベントを追加する
        self._events.append(OrderPaid(self._id, amount))


# アプリケーション層

class ReceiptSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: DomainEvent):
        pass


class PayOrderUseCase:
    def __init__(self, order_repo, user_repo, product_repo, dispatcher):
        self._order_repo = order_repo
        self._user_repo = user_repo
        self._product_repo = product_repo
        self._dispatcher = dispatcher

    def execute(self, order_id):
        #データ取得
        order = self._order_repo.get(order_id)
        user = self._user_repo.get(order.user_id)
        product = self._product_repo.get(order.product_id)

        #ビジネス処理
        price = order.calculate_price(product.price)

        user.pay(price)
        product.decrease_stock()
        order.mark_as_paid(price)

        #永続化
        self._user_repo.save(user)
        self._product_repo.save(product)
        self._order_repo.save(order)

        #イベント処理
        self._dispatcher.dispatch(order.events)
        order.clear_events()


# インフラ層
class EventDispatcher:
    def __init__(self):
        self._handlers = {}

    #外からイベントタイプとハンドラーを登録し、イベントが起こったときの連絡先を保持するメソッド
    #setdefaultは第一引数に指定したキーがすでに存在している場合は、第二引数にどんな値を指定しても辞書は元のまま変更されない配列追加メソッド
    #event_typeにはクラスが入る(OrderPaidなど)、handlerにはOrderPaidHandlerなどのインスタンスが入る
    def register(self, event_type, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    #eventsの中のイベントと_handlersの中のイベントタイプを比較し、同じ場合はハンドラーにメッセージを送る
    def dispatch(self, events):
        for event in events:
            for event_type, handlers in self._handlers.items():
                if isinstance(event, event_type):
                    for handler in handlers:
                        handler.handle(event)


#それぞれの方法(sender)で注文が支払われたことを通知するハンドラー
class OrderPaidHandler(EventHandler):
    #senderにはReceiptSenderを継承したクラスを渡す(EmailReceiptSenderなどの送信方法)
    def __init__(self, sender: ReceiptSender):
        self._sender = sender

    #各senderのsend()を呼び出す
    def handle(self, event: OrderPaid):
        self._sender.send(f"Payment completed: {event.amount}")


class EmailReceiptSender(ReceiptSender):
    def send(self, message: str):
        print("[EMAIL]", message)


#InMemory Repository
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._data = {}

    def get(self, order_id):
        return self._data[order_id.value]

    def save(self, order):
        self._data[order.id.value] = order


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._data = {}

    def get(self, user_id):
        return self._data[user_id]

    def save(self, user):
        self._data[user.id] = user


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._data = {}

    def get(self, product_id):
        return self._data[product_id]

    def save(self, product):
        self._data[product.id] = product
