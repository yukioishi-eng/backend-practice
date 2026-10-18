from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Session
from sql_practice.sqlalchemy.table_detail import Base, User
from datetime import date

def main():
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
    )

    #データの取得
    with Session(engine) as session:
        stmt = select(User).where(User.name == "田中")
        #データが1つだけの時(ユーザネームはユニーク制約があるので、データは1つのみ)
        user = session.scalars(stmt).one()
        #この戻り値はUserクラスのインスタンス
        print(user.id, user.name, user.birthday)

        #データが複数の時
        stmt = select(User)
        result = session.scalars(stmt)
        for user in result:
            print(user.name)
        #特にメソッドなどはない

        #条件式(特殊なもの)
        #None判定
        stmt = select(User).where(User.birthday.is_(None))
        #Noneじゃない場合はis_not()
        result = session.scalars(stmt)
        for user in result:
            print(user.name, user.birthday)

        #リスト
        stmt = select(User).where(User.name.in_(["鈴木", "茂木", "田中"]))
        result = session.scalars(stmt)
        for user in result:
            print(user.name, user.birthday)

        #パターン
        stmt = select(User).where(User.name.like("%木"))
        #likeの引数はワイルドカードで決まる
        result = session.scalars(stmt)
        for user in result:
            print(user.name, user.id)

        #並び替え
        stmt = select(User).order_by(User.birthday)
        #降順にするときは引数に.desc()をつける
        result = session.scalars(stmt)
        for user in result:
            print(user.name, user.birthday)

        #レコード制限
        stmt = select(User).limit(2)
        #上から2つ
        result = session.scalars(stmt)
        for user in result:
            print(user.name)

        #組み合わせ(メソッドチェーン)
        stmt = select(User).where(date(1990, 1, 1) < User.birthday).order_by(User.birthday)
        result = session.scalars(stmt)
        for user in result:
            print(user.name, user.birthday)
        #条件をANDにしたい時は,で区切る、ORにしたい時は,で区切って、or_()の中に入れる(sqlalchemyからor_のimportが必要)
        

if __name__ == "__main__":
    main()