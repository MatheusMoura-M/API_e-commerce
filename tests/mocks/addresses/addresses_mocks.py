class AddressesMocks:
    address_1 = {
        "number": 1,
        "street": "Rua1",
        "district": "Centro",
        "zipCode": "81000-000",
        "state": "SP",
        "city": "Santo André",
    }

    address_2 = {
        "number": 2,
        "street": "Rua2",
        "district": "Centro",
        "zipCode": "82000-000",
        "state": "CE",
        "city": "São Bernardo do Campo",
    }

    address_3 = {
        "number": 3,
        "street": "Rua3",
        "district": "Centro",
        "zipCode": "83000-000",
        "state": "SP",
        "city": "São Caetano",
    }

    address_fail_required_fields = {
        "street": "Rua1",
        "district": "Centro",
        "zipCode": 61,
        "state": "CE",
        "city": "Crato",
        "number": 48,
    }

    address_fail_wrong_types = {
        "street": "Rua1",
        "district": "Centro",
        "zipCode": 61,
        "state": "CE",
        "city": "Crato",
        "number": 48,
    }

    random_address = []
