class OrderFields:
    fields = ["id", "status", "created_at", "products_count", "products", "seller", "client"]
    read_only_fields = ["id", "seller", "client", "products"]
    extra_kwargs = {}
