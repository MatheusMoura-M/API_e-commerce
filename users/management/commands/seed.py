from django.core.management.base import BaseCommand
from typing import Any, Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserType
from products.models import Product
from addresses.models import Address
from carts.models import Cart
from tests.mocks.users import admin_mock, seller_mock
from tests.mocks.addresses import address_1_mock, address_2_mock
import random

User: UserType = get_user_model()


class Command(BaseCommand):
    help = "Criação de tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        import ipdb

        self.stdout.write(self.style.WARNING("seeding data... \n"))

        self.stdout.write(self.style.WARNING("creating users..."))

        addresses_data = [address_1_mock.address_1, address_2_mock.address_2]

        address_list = [
            Address.objects.create(**address_data) for address_data in addresses_data
        ]

        # ipdb.set_trace()
        users_data = [admin_mock.admin_data, seller_mock.seller_data]

        for i, _ in enumerate(users_data):
            users_data[i]["address"] = address_list[i]
            users_data[i]["cart"] = Cart.objects.create()

        users_list = [User.objects.create_user(**user_data) for user_data in users_data]

        print(users_list)
        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(users_list)} users created.]")
        )

        self.stdout.write(self.style.WARNING("creating products... \n"))

        sellers = User.objects.filter(is_seller=True)

        products_data = [
            {"name": "Doritos", "stock": 45, "category": "Alimentícios"},
            {"name": "Pão integral", "stock": 60, "category": "Alimentícios"},
        ]
        products_list = [
            Product(**product_data, user=random.choice(sellers))
            for product_data in products_data
        ]
        products_bulk = Product.objects.bulk_create(products_list)

        self.stdout.write(
            self.style.SUCCESS(f"Done! [{len(products_list)} products created.]")
        )
