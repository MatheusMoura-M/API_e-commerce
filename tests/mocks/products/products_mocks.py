import random


class ProductMocks:
    product_1 = {"name": "Doritos", "stock": 45, "category": "Alimentícios"}
    product_2 = {"name": "Pão integral", "stock": 60, "category": "Alimentícios"}
    product_without_stock = {"name": "Pão carioca", "stock": 0, "category": "Alimentícios"}

    product_fail = {}

    random_p = [
        {"name": "Arroz branco", "stock": 10, "category": "Alimentícios"},
        {"name": "Feijão preto", "stock": 12, "category": "Alimentícios"},
        {"name": "Macarrão espaguete", "stock": 13, "category": "Alimentícios"},
        {"name": "Óleo de soja", "stock": 1, "category": "Alimentícios"},
        {"name": "Açúcar refinado", "stock": 5, "category": "Alimentícios"},
        {"name": "Farinha de trigo", "stock": 6, "category": "Alimentícios"},
        {"name": "Sal refinado", "stock": 8, "category": "Alimentícios"},
        {"name": "Café em pó", "stock": 9, "category": "Alimentícios"},
        {"name": "Leite integral", "stock": 10, "category": "Alimentícios"},
        {"name": "Queijo mussarela", "stock": 3, "category": "Alimentícios"},
        {"name": "Margarina", "stock": 5, "category": "Alimentícios"},
        {"name": "Presunto fatiado", "stock": 8, "category": "Alimentícios"},
        {"name": "Peito de frango congelado", "stock": 1, "category": "Alimentícios"},
        {"name": "Sardinha em lata", "stock": 20, "category": "Alimentícios"},
        {"name": "Leite condensado", "stock": 17, "category": "Alimentícios"},
        {"name": "Achocolatado em pó", "stock": 14, "category": "Alimentícios"},
        {"name": "Biscoito de água e sal", "stock": 12, "category": "Alimentícios"},
        {"name": "Aveia em flocos", "stock": 11, "category": "Alimentícios"},
        {"name": "Linguiça calabresa defumada", "stock": 14, "category": "Alimentícios"},
        {"name": "Sabonete líquido antibacteriano", "stock": 12, "category": "Higiene"},
        {"name": "Shampoo para cabelos oleosos", "stock": 17, "category": "Higiene"},
        {"name": "Creme dental com flúor", "stock": 15, "category": "Higiene"},
        {"name": "Desodorante antitranspirante em aerosol", "stock": 12, "category": "Higiene"},
        {"name": "Papel higiênico com folhas duplas", "stock": 9, "category": "Higiene"},
        {"name": "Fio dental encerado", "stock": 7, "category": "Higiene"},
        {"name": "Hidratante corporal com vitamina E", "stock": 13, "category": "Higiene"},
        {"name": "Enxaguante bucal antisséptico", "stock": 4, "category": "Higiene"},
        {"name": "Absorvente feminino noturno", "stock": 11, "category": "Higiene"},
        {"name": "Algodão em disco para remover maquiagem", "stock": 27, "category": "Higiene"},
        {"name": "Camiseta de algodão orgânico", "stock": 12, "category": "Têxtil"},
        {"name": "Jeans skinny com elastano", "stock": 17, "category": "Têxtil"},
        {"name": "Camisa social de manga longa", "stock": 15, "category": "Têxtil"},
        {"name": "Blusa de lã merino", "stock": 12, "category": "Têxtil"},
        {"name": "Meias esportivas de cano alto", "stock": 9, "category": "Têxtil"},
        {"name": "Vestido midi de linho", "stock": 7, "category": "Têxtil"},
        {"name": "Lenço de seda estampado", "stock": 13, "category": "Têxtil"},
        {"name": "Tênis esportivo com cabedal em malha", "stock": 4, "category": "Têxtil"},
        {"name": "Jaqueta corta-vento de nylon", "stock": 11, "category": "Têxtil"},
        {"name": "Toalha de banho de algodão egípcio", "stock": 27, "category": "Têxtil"},
    ]

    def generate_price(products_db):
        products = []

        for product in products_db:
            product["price"] = round(random.uniform(1, 50), 2)
            products.append(product)
        return products

    random_products = generate_price(random_p)
