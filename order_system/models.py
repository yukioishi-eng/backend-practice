from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, Text, ForeignKey

class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True
    )

    balance: Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    orders: Mapped[list["OrderModel"]] = relationship(
        back_populates = "user"
    )

class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True 
    )

    price: Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    stock: Mapped[int] = mapped_column(
        Integer,
        nullable = False
    )

    orders: Mapped[list["OrderModel"]] = relationship(
        back_populates = "product"
    )
     

class OrderModel(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key = True,
        index = True
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable = False
    )

    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
        nullable = False
    )

    status: Mapped[str] = mapped_column(
        Text
    )

    paid_amount: Mapped[int] = mapped_column(
        Integer,
        default = 0
    )

    users: Mapped["UserModel"] = relationship(
        back_populates = "orders"
    )

    products: Mapped["ProductModel"] = relationship(
            back_populates = "orders"
    )