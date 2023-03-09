import uuid
from django.db import models
from products.models import Product


class Cart(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    products = models.ManyToManyField("products.Product", related_name="carts", through="carts.CartProducts")


class CartProducts(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
