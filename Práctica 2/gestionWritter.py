import os
from lxml import etree

xmlPath = os.path.dirname(__file__) + "\\XML\\"

casa_file = xmlPath + "insertions.xml"


def insert_new_entry(file, tag, attributes, sub_elements):
    tree = etree.parse(file)
    root = tree.getroot()

    # attributes = {"pito": "muy largo", "pelito": "demasiado"}

    new_element = etree.SubElement(root, tag, attributes)
    for i in sub_elements:
        etree.SubElement(sub_elements)


    tree.write(file, pretty_print=True)


personalidades = []
insert_new_entry(casa_file, "vecino", {"id": "01", "personalidad": "fantasma", "nombre": "Carlos", "casa": "066"}, [])
