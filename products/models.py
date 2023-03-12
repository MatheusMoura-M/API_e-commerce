from uuid import uuid4
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="products")
