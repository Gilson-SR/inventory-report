from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(products_list):
        manufacturing_date = min(
            [product["data_de_fabricacao"] for product in products_list]
        )
        expiration_date = min(
            [
                product["data_de_validade"]
                for product in products_list
                if product["data_de_validade"]
                >= datetime.now().strftime("%Y-%m-%d")
            ]
        )
        companies = {}
        for product in products_list:
            if product["nome_da_empresa"] in companies:
                companies[product["nome_da_empresa"]] += 1
            else:
                companies[product["nome_da_empresa"]] = 1
        larger_quantity_products = max(companies, key=companies.get)
        return (
            f"Data de fabricação mais antiga: {manufacturing_date}\n"
            f"Data de validade mais próxima: {expiration_date}\n"
            f"Empresa com mais produtos: {larger_quantity_products}"
        )
