from sqlalchemy import create_engine, inspect, select, update
from sqlalchemy.orm import Session, selectinload
from sql_practice.sqlalchemy.table_detail import Base, User
from datetime import date

def main():
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
    )

    #単一のテーブルを更新
    with Session(engine) as session:
        stmt = select(User).where(User.name == "田中")
        user = session.scalars(stmt).one()
        user.birthday = date(2002, 2, 4)
        session.commit()

    #複数のデータを更新
        stmt = update(User).where(User.birthday < date(2000, 1, 1)).values(birthday = date(2000, 12, 31))
        session.execute(stmt)
        session.commit()    

if __name__ == "__main__":
    main()