from datetime import datetime
from sqlalchemy import create_engine, delete, inspect, select
from sqlalchemy.orm import Session
from table_detail import Base, User, Post

def main():
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
    )

    #データの削除
    with Session(engine) as session:
        stmt = select(User).where(User.birthday.is_(None))
        user = session.scalars(stmt).one()
        session.delete(user)
        session.commit()
        #deleteもupdateと同じく、selectをdeleteにすることで、複数削除が可能

    # Postsテーブルのデータを全削除する
        stmt = delete(Post)
        session.execute(stmt)
        session.commit()

if __name__ == "__main__":
    main()