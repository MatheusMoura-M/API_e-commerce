from users.models import User
from rest_framework.exceptions import NotFound


def get_orders(products: list, user: User) -> list:
    orders = []

    for product in products:
        if not product.is_active or not product.stock:
            raise NotFound("The product is out of stock or not found in the database")

        product.stock -= 1
        product.is_active = product.stock != 0
        product.save()

        if not len(orders):
            order_create = {"client": user, "seller": product.user, "products": [product]}
            orders.append(order_create)
            continue

        for order in orders:
            if product.user.id == order["seller"].id:
                order["products"].append(product)
                break
            else:
                order_create = {"client": user, "seller": product.user, "products": [product]}
                orders.append(order_create)

    return orders
