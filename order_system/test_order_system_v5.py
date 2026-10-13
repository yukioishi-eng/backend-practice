import pytest

from fastapi.testclient import TestClient
from order_system.order_system_API import app, order_repo, user_repo, product_repo

from order_system.order_system_v5 import (
    Order,
    OrderId,
    OrderPaid,
    InMemoryOrderRepository,
    InMemoryUserRepository,
    InMemoryProductRepository,
    PayOrderUseCase,
    User,
    Product,
    EventDispatcher,
    OrderPaidHandler,
    EmailReceiptSender,
    InsufficientBalanceError,
    OutOfStockError,
)

def create_dispatcher():
    dispatcher = EventDispatcher()
    handler = OrderPaidHandler(EmailReceiptSender())
    dispatcher.register(OrderPaid, handler)
    return dispatcher


def test_pay_order_insufficient_balance():
    order_repo = InMemoryOrderRepository()
    user_repo = InMemoryUserRepository()
    product_repo = InMemoryProductRepository()

    dispatcher = create_dispatcher()

    user = User(user_id=1, balance=100)
    product = Product(product_id=1, price=300, stock=10)
    order = Order(OrderId(1), user_id=1, product_id=1)

    user_repo.save(user)
    product_repo.save(product)
    order_repo.save(order)

    usecase = PayOrderUseCase(order_repo, user_repo, product_repo, dispatcher)

    with pytest.raises(InsufficientBalanceError):
        usecase.execute(OrderId(1))


def test_pay_order_out_of_stock():
    order_repo = InMemoryOrderRepository()
    user_repo = InMemoryUserRepository()
    product_repo = InMemoryProductRepository()

    dispatcher = create_dispatcher()

    user = User(user_id=1, balance=1000)
    product = Product(product_id=1, price=300, stock=0)
    order = Order(OrderId(1), user_id=1, product_id=1)

    user_repo.save(user)
    product_repo.save(product)
    order_repo.save(order)

    usecase = PayOrderUseCase(order_repo, user_repo, product_repo, dispatcher)

    with pytest.raises(OutOfStockError):
        usecase.execute(OrderId(1))


def test_order_emits_event_on_payment():
    order = Order(OrderId(1), user_id=1, product_id=1)

    order.mark_as_paid(300)

    events = order.events

    assert len(events) == 1
    assert isinstance(events[0], OrderPaid)

#APIテスト
client = TestClient(app)

#注文の詳細取得
def test_get_order_success():
    res = client.get("/orders/1")
    assert res.status_code == 200
    assert res.json()["order_id"] == 1

#存在しない注文の詳細取得
def test_get_order_not_found():
    res = client.get("/orders/999")
    assert res.status_code == 404

#注文作成テスト
def test_create_order():
    res = client.post(
        "/orders", 
        json = {"order_id": 2, "user_id": 1, "product_id": 101}
    )
    assert res.status_code == 200

    #json形式のものにjson()をつけると、辞書型に変換される
    assert res.json()["message"] == "Order created successfully"
    assert res.json()["order_id"] == 2

#fixtureによるテストデータの準備
@pytest.fixture
def client_with_data():
    order_repo._data.clear()
    user_repo._data.clear()
    product_repo._data.clear()

    order_repo.save(Order(OrderId(1), user_id=1, product_id=101))
    user_repo.save(User(user_id=1, balance=5000))
    product_repo.save(Product(product_id=101, price=1000, stock=5))

    return TestClient(app)

#注文処理テスト
def test_pay_order_success(client_with_data):
    res = client_with_data.post("/orders/1/pay")
    assert res.status_code == 200
    assert res.json()["注文が完了しました"] == "PAID"

#存在しない注文の支払い
def test_pay_order_not_found(client_with_data):
    res = client_with_data.post("/orders/999/pay")
    assert res.status_code == 404

#残高不足のテスト
def test_pay_order_insufficient_balance(client_with_data):
    user = user_repo.get(1)
    user._balance = 0

    res = client_with_data.post("/orders/1/pay")
    assert res.status_code == 400
    assert res.json()["detail"] == "Insufficient user balance"

#在庫不足のテスト
def test_pay_order_out_of_stock(client_with_data):
    product = product_repo.get(101)
    product._stock = 0

    res = client_with_data.post("/orders/1/pay")
    assert res.status_code == 400
    assert res.json()["detail"] == "Product is out of stock"

