class UserFields:
    fields = [
        "id",
        "username",
        "email",
        "first_name",
        "password",
        "is_superuser",
        "is_seller",
        # "address",
        # "cart",
    ]
    read_only_fields = ["id", "is_superuser"]
    extra_kwargs = {"password": {"write_only": True}, "cart": {"write_only": True}}
