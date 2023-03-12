class UserFields:
    fields = ["id", "username", "first_name", "email", "password", "is_superuser", "is_seller", "address"]
    read_only_fields = ["id", "is_superuser"]
    extra_kwargs = {"password": {"write_only": True}}


class SellerFields:
    fields = ["id", "username", "first_name", "email"]
    read_only_fields = ["id"]
    extra_kwargs = {}


class ClientFields:
    fields = ["id", "username", "first_name", "email", "address"]
    read_only_fields = ["id"]
    extra_kwargs = {}
