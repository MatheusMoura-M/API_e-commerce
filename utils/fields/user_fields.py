class UserFields:
    fields = ["id", "username", "email", "first_name", "password", "is_superuser", "is_seller", "address"]
    read_only_fields = ["id", "is_superuser"]
    extra_kwargs = {"password": {"write_only": True}}


class SellerFields:
    fields = ["username", "email", "first_name", "is_seller"]
    read_only_fields = ["id"]
    extra_kwargs = {}


class ClientFields:
    fields = ["username", "email", "is_seller", "address"]
    read_only_fields = ["id"]
    extra_kwargs = {}
