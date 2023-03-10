from products.models import Product
from rest_framework.exceptions import NotFound


def get_products(products_data):
    products = []

    for product in products_data:
        try:
            instance_product = Product.objects.get(name__iexact=product["name"])

            products.append(instance_product)
        except Product.DoesNotExist:
            raise NotFound("Product not found.")

    return products
