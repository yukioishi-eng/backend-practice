from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Text, Uuid, Date, ForeignKey, DateTime
import uuid
from datetime import date, datetime
from zoneinfo import ZoneInfo

class Base(DeclarativeBase):
    pass

#sqlalchemyではテーブルをクラスで表現する
#Baseを継承することで、PythonのクラスとDBのテーブルを自動で紐付けてくれる
class User(Base):
    __tablename__ = "users"
    #テーブルのカラムはインスタンス変数として定義
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key = True,
        default = uuid.uuid4    #テーブルに登録した時に自動でidを割り当てる設定
    )

    name: Mapped[str] = mapped_column(
        Text, 
        nullable = False,
        unique = True
    )
    #Mappedは型ヒント、mapped_columnはデータベース上の制約（primary_key, nullable, defaultなど）を指定、nulllableは変数にNULLを許すかどうか

    birthday: Mapped[date] = mapped_column(
        Date,
        nullable = True
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates = "user"
    )
    #relationshipは外部キーなどのPythonのオブジェクト同士のつながりとして直感的に扱うための機能
    #よって、DBには関係ない
    #例えば、あるユーザの投稿一覧などをすぐに見れたりする


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[uuid.UUID] = mapped_column(
            Uuid, 
            primary_key = True,
            default = uuid.uuid4   
        )
    #記事のタイトル
    title: Mapped[str] = mapped_column(Text, nullable = False)
    #本文
    body: Mapped[str] = mapped_column(Text, nullable = False)
    #usersテーブルのidに紐づく外部キー
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"),
        #引数には紐づいているテーブル名.カラム名
        nullable = False
    )
    #投稿日時
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        default = lambda: datetime.now(ZoneInfo("Asia/Tokyo"))
    )
    #更新日時
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone = True),
        default = lambda: datetime.now(ZoneInfo("Asia/Tokyo")),
        #lambda式はコロン後の処理を呼び出す即席の関数のようなもの
        #本来はlambdaの後ろに関数に代入する変数があるが、関数を呼び出すだけなので、不要

        onupdate = lambda: datetime.now(ZoneInfo("Asia/Tokyo"))
        #カラムの内容が変更されるごとに記録し直す
    )
    #dateとdatetimeの違いは時刻が不要かどうか(更新日時などのログは秒まで必要)
    user: Mapped["User"] = relationship(
        back_populates = "posts"
    )