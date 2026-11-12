import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from order_system.database import Base
from order_system.use_case import PayOrderUseCase
from order_system.order_system_v5 import User, Product, Order, OrderId, OrderStatus, InsufficientBalanceError, OutOfStockError
from order_system.repositories import SQLAlchemyOrderRepository, SQLAlchemyProductRepository, SQLAlchemyUserRepository

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

def test_create_order_use_case(db_session):
    user_repo = SQLAlchemyUserRepository(db_session)
    product_repo = SQLAlchemyProductRepository(db_session)
    order_repo = SQLAlchemyOrderRepository(db_session)

    user = User(user_id = 1, balance = 5000)
    product = Product(product_id = 10, price = 1000, stock = 5)
    
    user_repo.save(user)
    product_repo.save(product)

    create_order_use_case = PayOrderUseCase(user_repo, product_repo, order_repo)
    create_order_use_case.execute(1, 10, 100)

    fatched_order = order_repo.get(OrderId(100))

    assert fatched_order.id == OrderId(100)
    assert fatched_order.product_id == 10
    assert fatched_order.user_id == 1
    assert fatched_order.status == OrderStatus.PAID
    assert fatched_order.paid_amount == 1000

def test_create_order_insufficient_balance(db_session):
    user_repo = SQLAlchemyUserRepository(db_session)
    product_repo = SQLAlchemyProductRepository(db_session)
    order_repo = SQLAlchemyOrderRepository(db_session)

    user = User(user_id = 1, balance = 500)
    product = Product(product_id = 10, price = 1000, stock = 5)
        
    user_repo.save(user)
    product_repo.save(product)

    create_order_use_case = PayOrderUseCase(user_repo, product_repo, order_repo)

    with pytest.raises(InsufficientBalanceError):
        create_order_use_case.execute(1, 10, 100)
    
def test_create_order_out_of_stock(db_session):
    user_repo = SQLAlchemyUserRepository(db_session)
    product_repo = SQLAlchemyProductRepository(db_session)
    order_repo = SQLAlchemyOrderRepository(db_session)

    user = User(user_id = 1, balance = 5000)
    product = Product(product_id = 10, price = 1000, stock = 0)
            
    user_repo.save(user)
    product_repo.save(product)
    
    create_order_use_case = PayOrderUseCase(user_repo, product_repo, order_repo)
    
    with pytest.raises(OutOfStockError):      
        create_order_use_case.execute(1, 10, 100)

    