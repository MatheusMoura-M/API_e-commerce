import uuid
from django.db import models


class StatusChoice(models.TextChoices):
    DEFAULT = "PEDIDO REALIZADO"
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=50, choices=StatusChoice.choices, default=StatusChoice.DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)

    seller = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders_sold")
    client = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders_bought")

    products = models.ManyToManyField("products.Product", related_name="orders", blank=True)
