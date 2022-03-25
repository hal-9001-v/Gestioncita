import os
from lxml import etree

xmlPath = os.path.dirname(__file__) + "\\XML\\"

casa_file = xmlPath + "Casas.xml"
coleccionable_file = xmlPath + "Coleccionables.xml"
edificio_file = xmlPath + "Edificios.xml"
equipable_file = xmlPath + "Equipable.xml"
isla_file = xmlPath + "Islas.xml"
jugada_file = xmlPath + "Islas.xml"
jugador_file = xmlPath + "Jugadores.xml"
materiales_file = xmlPath + "Materiales.xml"
mueble_file = xmlPath + "Muebles.xml"
personaje_file = xmlPath + "Personajes.xml"
prop_file = xmlPath + "Props.xml"
vecino_file = xmlPath + "Vecinos.xml"

use_test_output = True


def insert_new_entry(file, tag, attributes, sub_elements):
    tree = etree.parse(file)
    root = tree.getroot()

    # attributes = {"pito": "muy largo", "pelito": "demasiado"}

    new_element = etree.SubElement(root, tag, attributes)

    for i in sub_elements:
        etree.SubElement(sub_elements[i])

    # if not use_test_output:
    tree.write(file, pretty_print=True)


# Coleccionables
seasons = ["1", "2", "3", "4"]
specialType = ["1", "2", "3", "4"]
localizations = ["Cascada", "Estanque", "Mar", "Boca del rio", "Aire", "Tierra", "Flor", "Arbol", "Bajo tierra"]
rarities = ["1", "2", "3", "4", "5"]
id_count = 1

for season in seasons:
    for specialType in specialType:
        for localization in localizations:
            for rarity in rarities:
                attributes = {"id": "col" + str(id_count),
                              "tipoEsp": specialType,
                              "estacion": season,
                              "localizacion": localization,
                              "rareza": rarity}

                insert_new_entry(coleccionable_file, "coleccionable", attributes, [])
                id_count += 1
