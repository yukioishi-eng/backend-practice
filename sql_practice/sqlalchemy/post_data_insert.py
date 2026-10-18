from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session
from sql_practice.sqlalchemy.table_detail import Base, User, Post
from datetime import date

def main():
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
    )

    
    with Session(engine) as session:
        stmt1 = select(User).where(User.name == "田中")
        stmt2 = select(User).where(User.name == "鈴木")
        user = session.scalars(stmt1).one()
        user2 = session.scalars(stmt2).one()
        post_1 = Post(

            title = "Pythonについて",
            body = "Pythonはインタープリタ型の"
                   "高水準汎用プログラミング言語である。",
            user_id = user.id
        )

        post_2 = Post(
                    title = "Javaについて",
                    body = "Javaは汎用プログラミング言語"
                           "とソフトウェアプラットフォームの"
                           "双方を指している総省ブランドである。",
                    user_id = user.id
        )

        session.add_all([post_1, post_2])
        session.commit()
        post_1 = Post(
            title="PHPについて",
            body="PHPは The PHP Group によって"
            "コミュニティベースで開発されている"
            "オープンソースの汎用プログラミング言語",
            user_id=user.id
        )
        post_2 = Post(
            title="Rubyについて",
            body="Rubyはまつもとゆきひろにより開発された"
            "簡潔な文法が特徴的なオブジェクト指向スクリプト言語",
            user_id=user.id
        )
        session.add_all([post_1, post_2])
        session.commit()


if __name__  == "__main__":
    main()