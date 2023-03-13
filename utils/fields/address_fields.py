class AddressFields:
    fields = ["id", "street", "district", "zipCode", "state", "city", "number"]
    read_only_fields = ["id"]
    extra_kwargs = {}


class AddressWithoutIdFields:
    fields = ["street", "district", "zipCode", "state", "city", "number"]
    read_only_fields = []
    extra_kwargs = {}
