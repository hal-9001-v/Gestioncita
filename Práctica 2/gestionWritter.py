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
casas_of_vecinos_start = size_of_jugadores

# This would be called casas_left but it is unresolved reference then dont make questions ¯\_(ツ)_/¯
casas_avaliable = 30


def turn_id(id):
    if id >= 100:
        return str(id)
    if id >= 10:
        return "0" + str(id)

    return "00" + str(id)


def remove_previous(file):
    tree = etree.parse(file)
    root = tree.getroot()

    for child in root.getchildren():
        root.remove(child)

    tree.write(file, pretty_print=True)


def insert_new_entry(file, tag, attributes, sub_elements):
    tree = etree.parse(file)
    root = tree.getroot()

    new_element = etree.SubElement(root, tag, attributes)
    for sub in sub_elements:
        etree.SubElement(new_element, sub.tag, sub.attrib)

    tree.write(file, pretty_print=True)

    return new_element


def create_casas():
    casa_size = 369
    for i in range(casa_size):
        insert_new_entry(casa_file, "casa", {"id": "c" + turn_id(i)}, [])


def create_coleccionables():
    # Coleccionables
    seasons = ["Verano", "Otonio", "Invierno", "Primavera"]

    fosil_names = ["Craneo", "Amonites", "Hueso", "DinohHueso", "Nokia", "Trilobites"]
    pez_names = ["Carpa", "Palometa", "Pez Sable", "Tiburon", "Mero", "Ciluro"]
    insecto_names = ["Bicho palo", "Mariposa", "Hormiguita", "Mariquita", "Escarabajo", "Escararriba"]

    name_matrix = [fosil_names, pez_names, insecto_names]

    special_types = ["Fosil", "Pez", "Insecto"]
    adjectives = ["Celurio", "Curioso", "Interesante", "del Monton", "Peculiar", "Mono"]

    fosil_local = ["Tierra", "Bajo tierra"]
    insecto_local = ["Cascada", "Estanque", "Mar", "Boca del rio", "Aire", "Tierra", "Flor", "Arbol", "Bajo tierra"]
    pez_local = ["Cascada", "Estanque", "Mar", "Boca del rio", ]
    local_matrix = [fosil_local, pez_local, insecto_local]

    id_count = 0

    for j in range(300):
        special_type_i = random.randrange(0, 2)

        col_name = name_matrix[special_type_i][random.randrange(0, len(name_matrix[special_type_i]))] + " " + \
                   adjectives[random.randrange(0, len(adjectives))]
        local = local_matrix[special_type_i][random.randrange(0, len(local_matrix[special_type_i]))]

        attributes = {"id": "col" + turn_id(id_count),
                      "nombre": col_name,
                      "tamanio": str(random.randrange(1, 10)),
                      "tipoEsp": special_types[special_type_i],
                      "estacion": seasons[random.randrange(0, len(seasons))],
                      "localizacion": local,
                      "rareza": str(random.randrange(1, 5)),
                      "stack": "1",
                      "precio": str(random.randrange(10, 5000))}

        insert_new_entry(coleccionable_file, "coleccionable", attributes, [])
        id_count += 1


def create_edificios():
    # Care to give some correlation if global variable size_edificio!
    edificio_types = ["Ayuntamiento", "Peluqueria", "Supermercado", "Museo", "Aerodromo"]
    edificios_numbers = [1, 3, 10, 2, 1]
    id_counter = 0
    for i in range(len(edificio_types)):

        for j in range(edificios_numbers[i]):
            attributes = {"id": "ed" + turn_id(id_counter), "tipo": edificio_types[i]}
            insert_new_entry(edificio_file, "edificio", attributes, [])
            id_counter += 1


def create_equipables():
    # Equipables
    equip_count = 1
    equip_types = ["Ropa", "Herramienta"]
    equip_place = ["Mano", "Pie", "Espalda", "Torso", "Cabeza"]
    hats_names = ["Fedora", "Gorra", "Gorro", "Casco"]

    for hat in hats_names:
        random_price = random.randrange(100, 5000)
        attributes = {"id": "equi" + turn_id(equip_count), "nombre": hat,
                      "precio": str(random_price),
                      "tipo": equip_types[0], "lugar_eq": equip_place[4]}
        insert_new_entry(equipable_file, "equipable", attributes, [])
        equip_count += 1

    shoes_names = ["Botas", "Sneakers", "Chanclas", "Tacones", "Sandalia"]
    for shoes in shoes_names:
        random_price = random.randrange(100, 5000)
        attributes = {"id": "equi" + turn_id(equip_count), "nombre": shoes,
                      "precio": str(random_price),
                      "tipo": equip_types[0], "lugar_eq": equip_place[1]}
        insert_new_entry(equipable_file, "equipable", attributes, [])
        equip_count += 1

    chest_names = ["Gabardina", "Hawaiana", "Camisa", "Poncho", "Camisetita"]
    for chest in chest_names:
        random_price = random.randrange(100, 5000)
        attributes = {"id": "equi" + turn_id(equip_count), "nombre": chest,
                      "precio": str(random_price),
                      "tipo": equip_types[0], "lugar_eq": equip_place[3]}
        insert_new_entry(equipable_file, "equipable", attributes, [])
        equip_count += 1

    tools_names = ["Pala", "Pico", "Sarten", "Cazamariposas"]
    for tool in tools_names:
        random_price = random.randrange(100, 5000)
        attributes = {"id": "equi" + turn_id(equip_count), "nombre": tool,
                      "precio": str(random_price),
                      "tipo": equip_types[1], "lugar_eq": equip_place[0]}
        insert_new_entry(equipable_file, "equipable", attributes, [])
        equip_count += 1


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

        attributes = {"id": "is" + turn_id(i), "nombre": isla_names[i], "hemisferio": hemisferio}

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
                             {"id": "Edificios.xml#ed" + turn_id(i)})
            edificios_left -= 1
            edificios_in_isla += 1

        personaje_group = etree.SubElement(new_isla, "personajes", )
        for i in range(size_de_personajes):
            etree.SubElement(personaje_group, "personaje", {"id": "Personajes.xml#pj" + turn_id(i)})

        tree.write(isla_file, pretty_print=True)


def create_jugadores():
    jugadores_names = ["Pepito", "Fulanito", "Joselito", "Dio", "Vinsent", "Paquito", "Julia", "Marcela", "Castania",
                       "Milo", "Gatita", "Fidel", "Ernesto"]

    islas_left = size_islas
    for i in range(len(jugadores_names)):
        if islas_left == 0:
            islas_left = size_islas

        insert_new_entry(jugador_file, "jugador",
                         {"id": "j" + turn_id(i), "nombre": jugadores_names[i],
                          "isla": "Islas.xml#is" + turn_id(size_islas - islas_left),
                          "casa": "Casas.xml#c" + turn_id(casas_of_jugadores_start + i)}, [])
        islas_left -= 1


def create_materiales():
    # Materiales
    material_type = ["Piedra", "Pepita", "Madera", "Madera Dura", "Madera Blanda"]
    iterations = 5
    material_counter = 1

    for j in range(iterations):
        for i in range(len(material_type)):
            insert_new_entry(materiales_file, "material",
                             {"id": "mat" + turn_id(material_counter), "stack": str(random.randrange(10, 64)),
                              "precio": str(random.randrange(10, 500)), "tipoEsp": material_type[i]}, [])
            material_counter += 1


def create_muebles():
    # Muebles
    muebles_names = ["Mesita", "Sillita", "Lamparita", "Sofita"]
    mueble_tipos = ["Mesa", "Sillas y sofas", "Lampara", "Sillas y sofas"]
    mueble_conjuntos = ["", "Congelado", "Dorado", "Setas", "Flor de cerezo", "Bambu", "Mimbre", "Restaurante",
                        "Imperial",
                        "Flores", "Linda", "Mariana", "Veraniego", "Frutas", "Zodiaco", "Universitario"]
    adjectives = ["Mona", "Hortera", "Simple", "Elegante", "Epico", "Chuli"]

    iterations = 21
    mueble_counter = 0

    colors = ["Rojo", "Rosa", "Amarillo", "Azul", "Marron", "Morado", "Violeta", "Verde", "Lima", "Blanco", "Negro",
              "Gris", "Cian"]

    for j in range(iterations):
        for i in range(len(muebles_names)):
            random_price = random.randrange(50, 1000)

            conjunto = mueble_conjuntos[random.randrange(0, len(mueble_conjuntos))]
            mueble_name = muebles_names[i] + " " + adjectives[random.randrange(0, len(adjectives))]

            attributes = {"id": "mu" + turn_id(mueble_counter), "nombre": mueble_name, "stack": str(1),
                          "precio": str(random_price), "color": colors[random.randrange(0, len(colors))],
                          "tipo": mueble_tipos[i], "conjunto": conjunto}
            insert_new_entry(mueble_file, "mueble", attributes, [])
            mueble_counter += 1


def create_personajes():
    # Care to give some correlation with size_of_personajes
    personajes_names = ["Tom Nook", "Canela", "Rafa y Rodri", "Tendo y Nendo", "Sócrates", "Pili y Mili", "Figaro",
                        "El Capitan", "Alakama", "Alcatifa", "Al y Paca", "Betunio", "Buh", "CJ", "Conga", "Copito",
                        "Coti Conejal", "Estela", "Fauno", "Fran", "Gandulio", "Guindo", "Gulliver", "Gulliver Pirata",
                        "Juliana", "Camilo", "Katrina", "Ladino", "Marilin", "Pascal", "Renato", "Soponcio", "Totakeke",
                        "Tili", "Tortimer"]

    edificio_counter = 0
    for i in range(len(personajes_names)):

        if edificio_counter == size_edificios:
            edificio_counter = 0

        insert_new_entry(personaje_file, "personaje",
                         {"id": "pj" + turn_id(i), "nombre": personajes_names[i],
                          "edificio": "Edificios.xml#ed" + turn_id(edificio_counter)},
                         [])
        edificio_counter += 1


def create_props():
    # Props
    hierba_names = ["Cesped", "Hierbajo", "Ortiga"]

    flores_names = ["Petunia", "Margarita", "Rosa", "Jazmin"]
    arbustos_names = ["Romero", "Tomillo", "San Pedro", "Hiedra"]

    arboles_names = ["Manzano", "Naranjo", "Roble", "Pino", "Abeto", "Cedro", "Almendro", "Chopo"]

    frutas_names = ["Manzana", "Piña", "Coco", "Naranja", "Limon", "Lima"]

    props_types = ["Hierba", "Flor", "Piedra", "Arbusto", "Arbol", "Fruta"]

    piedras_names = ["Roca", "Menhir", "Caliza", "Carboncillo", "Piedra de rio"]

    names_matrix = [hierba_names, flores_names, piedras_names, arbustos_names, arboles_names, frutas_names]

    adjetivos = ["de Gran Belleza", "Normal", "con Defectos", "Esplendido", "como Ninguno", "Especial", "Mediocre"]

    prop_counter = 0

    for j in range(27):
        for i in range(5):

            if random.randrange(0, 2) == 1:
                random_stack = 10
            else:
                random_stack = 30

            random_price = random.randrange(100, 5000)
            name = names_matrix[i][random.randrange(0, len(names_matrix[i]))] + " " + adjetivos[random.randrange(0,
                                                                                                                 len(adjetivos))]

            if i == 4:
                comestible = "Si"
            else:
                comestible = "No"

            attributes = {"id": "prop" + turn_id(prop_counter), "nombre": name, "stack": str(random_stack),
                          "precio": str(random_price),
                          "tipo": props_types[i], "comestible": comestible}

            tree = etree.parse(prop_file)
            root = tree.getroot()

            new_element = etree.SubElement(root, "prop", attributes)
            etree.SubElement(new_element, "crecimiento").text = str(random.randrange(1, 5))

            tree.write(prop_file, pretty_print=True)
            prop_counter += 1


def get_vecino():
    # Vecinos
    nombres_vecinos = ["Paco", "Joshua", "Patri", "Marcelyn", "Apollo", "Steacy", "Carlos", "Queque", "Ariel",
                       "Narciso", "Munchi", "Morfeo", "Rosezna", "Luna", "Alderia", "Adela", "Agreste", "Alba",
                       "Albino", "Aliste", "Cabriola", "Cabralex", "Cachemir", "Camelio", "Babu", "Bambina", "Bayo",
                       "Bea", "Beelen", "Belinda", "Bella", "Benito", "Deira", "Dentina", "Dori", "Draco", "Dragonio",
                       "Deivid", "Fabiola", "Fardilla", "Fauna", "Feli", "Felipe" "Gabino", "Ganon", "Gaston",
                       "Hanalulu", "Hans", "Harpo", "Isadora", "Jacinto", "Jacobo", "Jaime", "Jairo", "Kabuki",
                       "Kaiman", "Kasandra", "Katia", "Lali", "Lanolina", "Lili", "Madam Rosa", "Magenta", "Marcial",
                       "Nabar", "Nachete", "Nana", "Narciso", "Octavio", "Octoberto", "Ofelia", "Pablo", "Paquito",
                       "Quetzal", "Radiolo", "Ramina", "Sabana", "Saltiago", "Sanson", "Tabita", "Talia", "Tami",
                       "Tania", "Ulises", "Uno", "Vacarena", "Wanda", "Wolfi", "Yuka", "Zapiron", "Zelanda"
                       ]
    personalidades = ["Alegre", "Atletico", "Esnob", "Dulce", "Grunion", "Presumido", "Perezoso", "Normal"]
    for i in range(len(nombres_vecinos)):
        attributes = {"id": "vec" + turn_id(i),
                      "personalidad": personalidades[random.randrange(0, len(personalidades))],
                      "nombre": nombres_vecinos[i],
                      "casa": "Casas.xml#c" + turn_id(casas_of_vecinos_start + i)}
        insert_new_entry(vecino_file, "vecino", attributes, [])


remove_previous(casa_file)
create_casas()

remove_previous(mueble_file)
create_muebles()

remove_previous(coleccionable_file)
create_coleccionables()

remove_previous(edificio_file)
create_edificios()

remove_previous(equipable_file)
create_equipables()

remove_previous(isla_file)
create_islas()

remove_previous(jugador_file)
create_jugadores()

remove_previous(materiales_file)
create_materiales()

remove_previous(personaje_file)
create_personajes()

remove_previous(prop_file)
create_props()

remove_previous(vecino_file)
create_vecinos()
