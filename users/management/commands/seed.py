from django.core.management.base import BaseCommand
from typing import Any, Optional

# from users.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserType
from products.models import Product

User: UserType = get_user_model()


class Command(BaseCommand):
    help = "Criação de tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write(self.style.WARNING("seeding data... \n"))

        admin_data = {
            "first_name": "Mariano",
            "username": "marianodias",
            "email": "marianodias@gmail.com",
            "password": "123123",
            "is_superuser": True,
        }

        users1_data = {
            "first_name": "Josival",
            "username": "josival123",
            "email": "josival123@gmail.com",
            "password": "123123",
            "is_seller": True,
        }

        self.stdout.write(self.style.WARNING("creating users..."))

        users_data = [admin_data, users1_data]
        users_list = [User.objects.create_user(**user_data) for user_data in users_data]

        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(users_list)} users created.]")
        )

        self.stdout.write(self.style.WARNING("creating products... \n"))

        products_data = [
            {"name": "Doritos", "stock": 45, "category": "Alimentícios"},
            {"name": "Pão integral", "stock": 60, "category": "Alimentícios"},
        ]
        products_list = [Product(**product_data) for product_data in products_data]
        products_bulk = Product.objects.bulk_create(products_list)

        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(products_list)} products created.]")
        )
