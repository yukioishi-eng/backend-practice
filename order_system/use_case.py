from order_system.order_system_v5 import Order, OrderStatus, OrderId, User, Product

class CreateOrderUseCase:
    def __init__(self, user_repo, product_repo, order_repo):
       self._user_repo = user_repo
       self._product_repo = product_repo
       self._order_repo = order_repo

    def execute(self, user_id: int, product_id: int, order_id: int) -> Order:
        user = self._user_repo.get(user_id)
        product = self._product_repo.get(product_id)

        user.pay(product.price)
        product.decrease_stock()

        self._user_repo.save(user)
        self._product_repo.save(product)

        order = Order(
            order_id = OrderId(order_id), 
            user_id = user.id, 
            product_id = product.id,
            status=OrderStatus.PAID,
            paid_amount=product.price
        )

        self._order_repo.save(order)

        return order