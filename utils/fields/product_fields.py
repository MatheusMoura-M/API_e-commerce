class ProductFields:
    fields = ["id", "name", "stock", "category", "price"]
    read_only_fields = ["id"]
    extra_kwargs = {}


class ProductOmitStockFields:
    fields = ["id", "name", "category", "price"]
    read_only_fields = ["id"]
    extra_kwargs = {}
