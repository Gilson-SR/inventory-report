import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        tree = ET.parse(path)
        roots = tree.getroot()
        stock = []
        for root in roots:
            item = {}
            for source in root:
                item[source.tag] = source.text
            stock.append(item)
        return stock
