from sqlalchemy import create_engine, inspect

def main():
    #データベースとの接続
    engine = create_engine(
        "sqlite:///C:/Users/31rek/backend-practice/sql_practice/sqlalchemy/pracitice.db",
        echo = True
        #sqllogを標準出力として表示
    )
    inspector = inspect(engine)
    print(inspector.get_table_names())    #テーブル一覧を表示

if __name__ == "__main__":
    main()