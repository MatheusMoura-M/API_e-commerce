class ProductFields:
    fields = [
        "id",
        "name",
        "stock",
        "category",
        "isActive",
    ]
    read_only_fields = ["id"]
    extra_kwargs = {}
