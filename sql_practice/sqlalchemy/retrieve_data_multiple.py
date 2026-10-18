from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session, selectinload
from sql_practice.sqlalchemy.table_detail import Base, User
from datetime import date

def main():
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
    )

    #複数のテーブルのデータを取得
    with Session(engine) as session:
        stmt = select(User).options(selectinload(User.posts))
        result = session.scalars(stmt)
        for user in result:
            for post in user.posts:
                print(user.name, post.title)
    #PostからもUserを呼び出せる
    #selectinloadはn + 1問題に対処する方法(selectの呼び出しが少ない)
        

if __name__ == "__main__":
    main()