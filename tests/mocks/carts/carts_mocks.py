class CartMocks:
    cart_1 = {
        "products": [
            {"name": "Arroz branco"},
            {"name": "Feijão preto"},
            {"name": "Algodão em disco para remover maquiagem"},
            {"name": "Jaqueta corta-vento de nylon"},
        ]
    }

    cart_2 = {
        "products": [
            {"name": "Papel higiênico com folhas duplas"},
            {"name": "Leite condensado"},
            {"name": "Hidratante corporal com vitamina E"},
            {"name": "Jaqueta corta-vento de nylon"},
        ]
    }

    cart_3 = {
        "products": [
            {"name": "Absorvente feminino noturno"},
            {"name": "Algodão em disco para remover maquiagem"},
            {"name": "Camiseta de algodão orgânico"},
            {"name": "Jeans skinny com elastano"},
        ]
    }

    cart_fail_required_fields = {}

    cart_fail_product_not_found = {
        "products": [
            {
                {"name": "ZZZZZZZZZZ", "stock": 11, "category": "Higiene"},
                {"name": "Algodão em disco para remover maquiagem", "stock": 27, "category": "Higiene"},
                {"name": "Camiseta de algodão orgânico", "stock": 12, "category": "Têxtil"},
                {"name": "Jeans skinny com elastano", "stock": 17, "category": "Têxtil"},
            },
        ]
    }
