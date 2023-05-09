import csv
import json
import xml.etree.ElementTree as ET

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def _load_csv(path):
        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    @staticmethod
    def _load_json(path):
        with open(path) as file:
            return json.load(file)

    @staticmethod
    def _load_xml(path):
        tree = ET.parse(path)
        roots = tree.getroot()
        stock = []
        for root in roots:
            item = {}
            for source in root:
                item[source.tag] = source.text
            stock.append(item)
        return stock

    @staticmethod
    def import_data(path, report_type):
        loaders = {
            "csv": Inventory._load_csv,
            "json": Inventory._load_json,
            "xml": Inventory._load_xml,
        }

        if report_type == "simples":
            generator = SimpleReport.generate
        elif report_type == "completo":
            generator = CompleteReport.generate
        else:
            raise ValueError("Tipo de relatório inválido")

        extension = path.split(".")[-1]
        if extension not in loaders:
            raise ValueError("Extensão de arquivo inválida")

        stock = loaders[extension](path)
        report = generator(stock)
        return report
