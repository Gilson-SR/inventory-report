import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        extension = path.split(".")[-1]
        if extension == "csv":
            with open(path, newline='') as file:
                reader = csv.DictReader(file)
                stock = [row for row in reader]
        elif extension == "json":
            with open(path) as file:
                stock = json.load(file)
        else:
            raise ValueError("Extensão de arquivo inválida")

        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report
