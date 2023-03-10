import uuid
from django.db import models


class Order(models.Model):
    class StatusChoice(models.TextChoices):
        PEDIDOREALIZADO = " PEDIDO REALIZADO"
        EMANDAMENTO = "EM ANDAMENTO"
        ENTREGUE = "ENTREGUE"
        
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=50, choices=StatusChoice)
    users_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
    createAt = models.DateField(null=True, blank=True)