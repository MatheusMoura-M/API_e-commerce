from users.models import User
from rest_framework.exceptions import NotFound
from orders.models import Order


def get_orders(products: list, user: User) -> list:
    orders = []

    for product in products:
        if not product.is_active or not product.stock:
            raise NotFound("The product is out of stock or not found in the database")

        product.stock -= 1
        product.is_active = product.stock != 0
        product.save()

        var = False
        for order in orders:
            if product.user.id == order["seller"].id:
                var = True
                order["products"].append(product)

        if not var:
            order_create = {
                "client": user,
                "seller": product.user,
                "products": [product],
            }
            orders.append(order_create)

    return orders


def create_orders(orders: list):
    orders_return = []

    for order in orders:
        instance_order = Order.objects.create(
            client=order["client"], seller=order["seller"]
        )

        instance_order.products.set(order["products"])
        instance_order.save()

        orders_return.append(instance_order)

    return orders_return
