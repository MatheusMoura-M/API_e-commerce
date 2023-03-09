class ProductFields:
    fields = [
        "id",
        "name",
        "stock",
        "category",
        "is_active",
    ]
    read_only_fields = ["id"]
    extra_kwargs = {}
