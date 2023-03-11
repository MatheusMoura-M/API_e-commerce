class OrderFields:
    fields = ["id", "status", "seller", "client", "created_at", "products"]
    read_only_fields = ["id", "seller", "client", "products"]
    extra_kwargs = {}
