import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from order_system.database import Base
from order_system.models import UserModel, ProductModel, OrderModel
from order_system.repositories import (
    SQLAlchemyUserRepository,
    SQLAlchemyProductRepository,
    SQLAlchemyOrderRepository
)
from order_system.order_system_v5 import User, Product, Order, OrderStatus, OrderId

@pytest.fixture
def db_session():
    #テスト専用のメモリ上データベースを作成
    engine = create_engine(
        "sqlite:///:memory:", 
        connect_args = {"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit = False, 
        autoflush = False, 
        bind = engine
    )
    
    
    Base.metadata.create_all(engine)
    
    #テスト用のセッションを開いてテスト関数に渡す
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


#テストケース
def test_user_repository_save_and_get(db_session):
    repo = SQLAlchemyUserRepository(db_session)
    
    user = User(user_id=1, balance=3000)
    repo.save(user)
    
    fetched_user = repo.get(1)
    
    assert fetched_user.id == 1
    assert fetched_user.balance == 3000


def test_product_repository_save_and_get(db_session):
    repo = SQLAlchemyProductRepository(db_session)
    
    product = Product(product_id=10, price=500, stock=20)
    repo.save(product)
    
    fetched_product = repo.get(10)
    
    assert fetched_product.id == 10
    assert fetched_product.price == 500
    assert fetched_product.stock == 20

def test_order_repository_save_and_get(db_session):
    user_repo = SQLAlchemyUserRepository(db_session)
    product_repo = SQLAlchemyProductRepository(db_session)
    order_repo = SQLAlchemyOrderRepository(db_session)

    user = User(user_id = 1, balance = 5000)
    product = Product(product_id = 10, price = 1000, stock = 5)
    order = Order(
        order_id = OrderId(100),
        user_id = 1,
        product_id = 10,
    )
    user_repo.save(user)
    product_repo.save(product)
    order_repo.save(order)

    fatched_order = order_repo.get(OrderId(100))

    assert fatched_order.id.value == 100
    assert fatched_order.user_id == 1
    assert fatched_order.product_id == 10
    assert fatched_order.status == OrderStatus.CREATED