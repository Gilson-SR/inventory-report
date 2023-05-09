from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products_list):
        simple_report = SimpleReport.generate(products_list)

        companies = {}

        for product in products_list:
            company = product["nome_da_empresa"]
            if company in companies:
                companies[company] += 1
            else:
                companies[company] = 1

        label_products_company = "Produtos estocados por empresa:\n"

        for company in companies:
            label_products_company += f"- {company}: {companies[company]}\n"

        return (
            f"{simple_report}\n"
            f"{label_products_company}"
        )
