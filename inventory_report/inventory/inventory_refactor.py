from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def define_type(report_type, stock):
        if report_type == "simples":
            report = SimpleReport.generate(stock)
        elif report_type == "completo":
            report = CompleteReport.generate(stock)
        else:
            raise ValueError("Tipo de relatório inválido")

        return report

    @staticmethod
    def import_data(path, report_type):
        extension = path.split(".")[-1]
        if extension == "csv":
            importer = CsvImporter()
        elif extension == "json":
            importer = JsonImporter()
        elif extension == "xml":
            importer = XmlImporter()
        else:
            raise ValueError("Extensão de arquivo inválida")

        stock = importer.import_data(path)

        return Inventory.define_type(report_type, stock)
