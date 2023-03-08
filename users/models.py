import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from addresses.models import Address
from carts.models import Cart


class User(AbstractUser):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(null=True, default=False)

    # address = models.OneToOneField(Address, related_name="user", on_delete=models.CASCADE)
    # cart = models.OneToOneField(Cart, related_name="user", on_delete=models.CASCADE)
