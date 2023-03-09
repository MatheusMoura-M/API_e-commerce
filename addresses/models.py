import uuid
from django.db import models


class Address(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street = models.CharField(max_length=50)
    distric = models.CharField(max_length=50)
    zipCode = models.IntegerField()
    number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
