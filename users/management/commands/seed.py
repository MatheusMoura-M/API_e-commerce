import random
from carts.models import Cart
from typing import Any, Optional
from products.models import Product
from addresses.models import Address
from django.contrib.auth import get_user_model
from django.core.management import call_command
from tests.mocks.users.users_mocks import UserMocks
from django.core.management.base import BaseCommand
from tests.mocks.users.client_mock import client_data
from tests.mocks.users.seller_mock import seller_data
from django.contrib.auth.models import User as UserType
from tests.mocks.addresses.addresses_mocks import AddressesMocks
from tests.mocks.products.products_mocks import ProductMocks

User: UserType = get_user_model()


class Command(BaseCommand):
    help = "Criação de tests"

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        users_data = UserMocks.random_users + [client_data, seller_data]
        products_data = ProductMocks.random_products
        addresses_data = AddressesMocks.random_addresses

        self.stdout.write(self.style.WARNING("seeding data... \n"))
        self.stdout.write(self.style.WARNING("creating admins...\n"))

        call_command("create_admin")
        call_command("create_admin", username="marianodias", password="123123", email="marianodias@gmail.com")

        self.stdout.write(self.style.SUCCESS(f"Done! [{2} admin created.] \n"))

        self.stdout.write(self.style.WARNING("creating users... \n"))

        address_list = [Address(**address_data) for address_data in addresses_data]
        address_created = Address.objects.bulk_create(address_list)

        for i, user in enumerate(users_data):
            user["cart"] = Cart.objects.create()
            user["address"] = address_created[i]

        users_list = []

        for user_data in users_data:
            user = User(**user_data)
            user.set_password(user_data["password"])
            users_list.append(user)

        User.objects.bulk_create(users_list)

        self.stdout.write(self.style.SUCCESS(f"Done! [{len(users_list)} users created.] \n "))

        self.stdout.write(self.style.WARNING("creating products... \n"))

        sellers = User.objects.filter(is_seller=True)

        products_list = [Product(**product_data, user=random.choice(sellers)) for product_data in products_data]
        Product.objects.bulk_create(products_list)

        self.stdout.write(self.style.SUCCESS(f"Done! [{len(products_list)} products created.]\n "))
