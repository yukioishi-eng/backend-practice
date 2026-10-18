from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session
from sql_practice.sqlalchemy.table_detail import Base, User
from datetime import date

def main():
    #データベースとの接続
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
        echo = True
    )

    #データの追加
    #単体
    with Session(engine) as session:
        user = User(name = "鈴木", birthday = date(1991, 1, 1))
        session.add(user)

        #複数
        user1 = User(name = "田中", birthday = date(2004, 2, 23))
        user2 = User(name = "茂木", birthday = date(1989, 10, 31))
        user3 = User(name = "張本")
        session.add_all([user1, user2, user3])
        session.commit()

if __name__ == "__main__":
    main()