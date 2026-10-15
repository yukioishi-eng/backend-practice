import sys
from pathlib import Path

from sqlalchemy import create_engine, inspect

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from main import Base

def main():
    #データベースとの接続
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
        echo = True
        #sqllogを標準出力として表示
    )
    Base.metadata.create_all(engine)
    #Baseを継承しているクラスの定義からテーブルを作成する(sqlでいうCREATE TABLE)

if __name__ == "__main__":
    main()