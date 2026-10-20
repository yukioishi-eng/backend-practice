from sqlalchemy import create_engine, inspect
from order_system.models import Base

def main():
    engine = create_engine( "sqlite:///C:/Users/31rek/backend-practice/order_system/order_system.db",
    echo = True
    )

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()