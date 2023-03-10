from uuid import uuid4
from django.db import models


class Product(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
