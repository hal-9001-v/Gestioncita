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

size_of_jugadores = 5
size_edificios = 5
size_de_personajes = 3
size_islas = 5
size_of_vecinos = 8

size_of_casas = size_of_jugadores + size_of_vecinos
casas_of_jugadores_start = 0
casas_of_vecinos_start = size_de_personajes

# This would be called casas_left but it is unresolved reference then dont make questions ¯\_(ツ)_/¯
casas_avaliable = 30


def insert_new_entry(file, tag, attributes, sub_elements):
    tree = etree.parse(file)
    root = tree.getroot()

    new_element = etree.SubElement(root, tag, attributes)
    for sub in sub_elements:
        etree.SubElement(new_element, sub.tag, sub.attrib)

    tree.write(file, pretty_print=True)

    return new_element


def create_casas():
    casa_size = 30
    for i in range(casa_size):
        insert_new_entry(casa_file, "casa", {"id": "c" + str(i)}, [])


def create_coleccionables():
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


def create_edificios():
    # Care to give some correlation if global variable size_edificio!
    edificio_types = ["Ayuntamiento", "Peluqueria", "Supermercado", "Museo", "Aerodromo"]
    for i in range(len(edificio_types)):
        attributes = {"id": "ed" + str(i), "tipo": edificio_types[i]}
        insert_new_entry(edificio_file, "edificio", attributes, [])


def create_equipables():
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


def create_islas():
    # Islas
    isla_names = ["AlcorOn", "SouthPeru", "MostToLess", "TorriHoes", "WestMadriz"]

    sub_personajes = ["5", "6"]
    edificios_left = size_edificios
    for i in range(len(isla_names)):
        if i % 2 == 0:
            hemisferio = "N"
        else:
            hemisferio = "S"

        attributes = {"id": "is" + str(i), "nombre": isla_names[i], "hemisferio": hemisferio}

        tree = etree.parse(isla_file)
        root = tree.getroot()

        new_isla = etree.SubElement(root, "isla", attributes)

        fecha = etree.SubElement(new_isla, "fecha", )
        random_day = str(random.randrange(1, 28))
        random_month = str(random.randrange(1, 12))
        fecha.text = random_day + "-" + random_month + "-2022"

        hora = etree.SubElement(new_isla, "hora", )
        random_hour = str(random.randrange(0, 23))
        random_minute = str(random.randrange(10, 59))

        hora.text = random_hour + ":" + random_minute

        edificio_group = etree.SubElement(new_isla, "edificios", )
        edificios_in_isla = 0

        for i in range(size_edificios):
            etree.SubElement(edificio_group, "edificio",
                             {"id": "Edificios.xml#ed" + str(i)})
            edificios_left -= 1
            edificios_in_isla += 1

        personaje_group = etree.SubElement(new_isla, "personajes", )
        for i in range(size_de_personajes):
            etree.SubElement(personaje_group, "personaje", {"id": "Personajes.xml#pj" + str(i)})

        tree.write(isla_file, pretty_print=True)


def create_jugadores():
    jugadores_names = ["Pepito", "Fulanito", "Joselito", "Dio", "Vinsent"]

    islas_left = size_islas
    for i in range(len(jugadores_names)):
        if islas_left == 0:
            islas_left = size_islas

        insert_new_entry(jugador_file, "jugador",
                         {"id": "j" + str(i), "nombre": jugadores_names[i],
                          "isla": "Islas.xml#is" + str(size_islas - islas_left),
                          "casa": "Casas.xml#c" + str(casas_of_jugadores_start + i)}, [])


def create_materiales():
    # Materiales
    material_type = ["Piedra", "Pepita", "Madera", "Madera Dura", "Madera Blanda"]
    for i in range(len(material_type)):
        insert_new_entry(materiales_file, "material", {"id": "mat" + str(i), "tipoEsp": material_type[i]}, [])


def create_muebles():
    # Muebles
    muebles_names = ["Mesita", "Sillita", "Lamparita", "Sofita"]
    mueble_tipos = ["Mesa", "Sillas y sofas", "Lampara", "Sillas y sofas"]
    mueble_conjuntos = ["", "Congelado", "Dorado", "Setas", "Flor de cerezo", "Bambu", "Mimbre", "Restaurante",
                        "Imperial",
                        "Flores", "Linda", "Mariana", "Veraniego", "Frutas", "Zodiaco", "Universitario"]
    for i in range(len(muebles_names)):
        random_stack = random.randrange(1, 64)
        random_price = random.randrange(100, 5000)

        attributes = {"id": "mu" + str(i), "nombre": muebles_names[i], "stack": str(random_stack),
                      "precio": str(random_price), "tipo": mueble_tipos[i], "conjunto": mueble_conjuntos[i]}
        insert_new_entry(mueble_file, "mueble", attributes, [])


def create_personajes():
    # Care to give some correlation with size_of_personajes
    personajes_names = ["Tom Nook", "Canela", "Rafa"]
    edificios_of_personajes = ["1", "1", "2"]
    for i in range(len(personajes_names)):
        insert_new_entry(personaje_file, "personaje",
                         {"id": "pj" + str(i), "nombre": personajes_names[i],
                          "edificio": "Edificios.xml#ed" + edificios_of_personajes[i]},
                         [])


def create_props():
    # Props
    props_names = ["Cesped", "Petunia", "Roca", "Romero", "Manzano", "Naranja"]
    props_types = ["Hierba", "Flor", "Piedra", "Arbusto", "Arbol", "Fruta"]
    comestibles = ["No", "No", "No", "No", "No", "Si"]
    for i in range(len(props_names)):
        random_stack = random.randrange(1, 64)
        random_price = random.randrange(100, 5000)
        attributes = {"id": "prop" + str(i), "nombre": props_names[i], "stack": str(random_stack),
                      "precio": str(random_price),
                      "tipo": props_types[i], "comestible": comestibles[i]}
        insert_new_entry(prop_file, "prop", attributes, [])


def create_vecinos():
    # Vecinos
    nombres_vecinos = ["Paco", "Joshua", "Ankha", "Marcelyn", "Apollo", "Steacy", "Carlos", "Queque"]
    personalidades = ["Alegre", "Atletico", "Esnob", "Dulce", "Grunion", "Presumido", "Perezoso", "Normal"]
    for i in range(len(nombres_vecinos)):
        attributes = {"id": "vec" + str(i), "personalidad": personalidades[i], "nombre": nombres_vecinos[i],
                      "casa": "Casas.xml#c" + str(casas_of_vecinos_start + i)}
        insert_new_entry(vecino_file, "vecino", attributes, [])


create_casas()

create_coleccionables()

create_edificios()

create_equipables()

create_islas()

create_jugadores()

create_materiales()

create_personajes()

create_props()

create_vecinos()
