from products.models import Product
from rest_framework.exceptions import NotFound


def get_products(products_data):
    products = []

    for product in products_data:
        try:
            product_instance = Product.objects.get(name_iexact=product.name)

            products.append(product_instance)
        except Product.DoesNotExist:
            raise NotFound("Product not found.")

    return products
