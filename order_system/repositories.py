from sqlalchemy.orm import Session
from order_system.models import OrderModel, UserModel, ProductModel
from order_system.order_system_v5 import OrderRepository, UserRepository, ProductRepository, OrderId, Order, OrderStatus, User, Product

class SQLAlchemyOrderRepository(OrderRepository):
    def __init__(self, session: Session):
        self._session = session

    
    def get(self, orderid: OrderId) -> Order:
        model = self._session.get(OrderModel, orderid.value)
        if model is None:
            raise KeyError("Order not found")
        
        order = Order(
            order_id=OrderId(model.id),
            user_id=model.user_id,
            product_id=model.product_id
        )
        #model.statusが文字列ならEnum型に変換して,それ以外ならそのまま代入(statusの管理がEnum型だから)
        order._status = OrderStatus[model.status] if isinstance(model.status, str) else model.status
        order._paid_amount = model.paid_amount

        return order

    def save(self, order: Order) -> None:
        model = self._session.get(OrderModel, order.id.value)
        
        if model is None:
            model = OrderModel(
                id = order.id.value,
                user_id = order.user_id,
                product_id = order.product_id,
                status = order.status.name,
                paid_amount = order._paid_amount  
            )
            self._session.add(model)
        else:
            model.id = order.id.value
            model.user_id = order.user_id
            model.product_id = order.product_id
            model.status = order.status.name
            model.paid_amount = order._paid_amount  
        self._session.commit()

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: Session):
            self._session = session

    def get(self, user_id: int) -> User:
        model = self._session.get(UserModel, user_id)
        if model is None:
            raise KeyError("user not found")

        user = User(
            user_id = model.id,
            balance = model.balance
        )
        return user

    def save(self, user: User) -> None:
        model = self._session.get(UserModel, user.id)
        if model is None:
            model = UserModel(
                id = user.id,
                balance = user._balance
            )
            self._session.add(model)

        else:
           model.id = user.id
           model.balance = user.balance 

        self._session.commit()

class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self._session = session

    def get(self, product_id: int) -> Product:
        model = self._session.get(ProductModel, product_id)
        if model is None:
            raise KeyError("product not found")

        product = Product(
            product_id = model.id,
            price = model.price,
            stock = model.stock
        )
        return product

    def save(self, product: Product) -> None:
        model = self._session.get(ProductModel, product.id)
        if model is None:
            model = ProductModel(
                id = product.id,
                price = product.price,
                stock = product.stock
            )
            self._session.add(model)

        else:
           model.id = product.id
           model.price = product.price
           model.stock = product.stock

        self._session.commit()
