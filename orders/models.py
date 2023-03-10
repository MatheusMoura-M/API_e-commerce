import uuid
from django.db import models


class StatusChoice(models.TextChoices):
    EM_ANDAMENTO = "EM ANDAMENTO"
    ENTREGUE = "ENTREGUE"
    DEFAULT = "PEDIDO REALIZADO"


class Order(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    status = models.CharField(
        max_length=50, choices=StatusChoice.choices, default=StatusChoice.DEFAULT
    )
    createdAt = models.DateField(null=True, blank=True)
