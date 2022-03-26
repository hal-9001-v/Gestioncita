import os
import random

from lxml import etree

xmlPath = os.path.dirname(__file__) + "\\XML\\"

casa_file = xmlPath + "Casas.xml"
coleccionable_file = xmlPath + "Coleccionables.xml"
edificio_file = xmlPath + "Edificios.xml"
equipable_file = xmlPath + "Equipables.xml"
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
    for sub in sub_elements:
        etree.SubElement(new_element, sub.tag, sub.attrib)

    # if not use_test_output:
    tree.write(file, pretty_print=True)

    return new_element


# Casas
casa_size = 30
for i in range(casa_size):
    insert_new_entry(casa_file, "casa", {"id": "c" + str(i)}, [])

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

# Edificios
edificio_types = ["Ayuntamiento", "Peluqueria", "Supermercado", "Museo", "Aerodromo"]
for i in range(len(edificio_types)):
    attributes = {"id": "ed" + str(i), "tipo": edificio_types[i]}
    insert_new_entry(edificio_file, "edificio", attributes, [])

# Equipables
equip_count = 1
equip_types = ["Ropa", "Herramienta"]
equip_place = ["Mano", "Pie", "Espalda", "Torso", "Cabeza"]
hats_names = ["Fedora", "Gorra", "Gorro", "Casco"]

for hat in hats_names:
    random_stack = random.randrange(1, 64)
    random_price = random.randrange(100, 5000)
    attributes = {"id": "equi" + str(equip_count), "nombre": hat, "stack": str(random_stack),
                  "precio": str(random_price),
                  "tipo": equip_types[0], "lugar_eq": equip_place[4]}
    insert_new_entry(equipable_file, "equipable", attributes, [])

shoes_names = ["Botas", "Sneakers", "Chanclas", "Tacones", "Sandalia"]
for shoes in shoes_names:
    random_stack = random.randrange(1, 64)
    random_price = random.randrange(100, 5000)
    attributes = {"id": "equi" + str(equip_count), "nombre": shoes, "stack": str(random_stack),
                  "precio": str(random_price),
                  "tipo": equip_types[0], "lugar_eq": equip_place[1]}
    insert_new_entry(equipable_file, "equipable", attributes, [])

chest_names = ["Gabardina", "Hawaiana", "Camisa", "Poncho", "Camisetita"]
for chest in chest_names:
    random_stack = random.randrange(1, 64)
    random_price = random.randrange(100, 5000)
    attributes = {"id": "equi" + str(equip_count), "nombre": chest, "stack": str(random_stack),
                  "precio": str(random_price),
                  "tipo": equip_types[0], "lugar_eq": equip_place[3]}
    insert_new_entry(equipable_file, "equipable", attributes, [])

tools_names = ["Pala", "Pico", "Sarten", "Cazamariposas"]
for tool in tools_names:
    random_stack = random.randrange(1, 64)
    random_price = random.randrange(100, 5000)
    attributes = {"id": "equi" + str(equip_count), "nombre": tool, "stack": str(random_stack),
                  "precio": str(random_price),
                  "tipo": equip_types[1], "lugar_eq": equip_place[0]}
    insert_new_entry(equipable_file, "equipable", attributes, [])


#Islas
isla_names = ["AlcorOn", "SouthPeru", "MostToLess", "TorriHoes", "WestMadriz"]
sub_edificios = ["120", "135"]
sub_personajes = ["5", "6"]
for i in range(len(isla_names)):
    if i % 2 == 0:
        hemisferio = "N"
    else:
        hemisferio = "S"

    attributes = {"id": "is" + str(i), "nombre": isla_names[i], "hemisferio": hemisferio}

    tree = etree.parse(isla_file)
    root = tree.getroot()

    new_isla = etree.SubElement(root, "isla", attributes)

    edificio_group = etree.SubElement(new_isla, "edificios", )
    for sub in sub_edificios:
        etree.SubElement(edificio_group, "edificio", {"id": "Edificios.xml#ed" + sub})

    personaje_group = etree.SubElement(new_isla, "personajes", )
    for sub in sub_personajes:
        etree.SubElement(personaje_group, "personaje", {"id": "Personajes.xml#ed" + sub})

#Jugadores


tree.write(isla_file, pretty_print=True)
