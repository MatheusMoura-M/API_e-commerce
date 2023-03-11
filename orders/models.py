import uuid
from django.db import models


class StatusChoice(models.TextChoices):
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"
    DEFAULT = "PEDIDO REALIZADO"


class Order(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    client = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders_bought"
    )
    seller = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders_sold"
    )
    status = models.CharField(
        max_length=50, choices=StatusChoice.choices, default=StatusChoice.DEFAULT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        "products.Product", related_name="orders", blank=True
    )