import os
import json
import random


class InventoryObject:
    def __init__(self, objetoId, nombre, stack, precio, tipo, tipoEsp):
        self.objetoId = objetoId
        self.nombre = nombre
        self.stack = stack
        self.precio = precio
        self.tipo = tipo
        self.tipoEsp = tipoEsp

    def get_json(self):
        return json.dumps(self.getDict())

    def get_dict(self):
        dict_values = {"objetoId": self.objetoId,
                       "nombre": self.nombre,
                       "stack": self.stack,
                       "precio": self.precio,
                       "tipo": self.tipo,
                       "tipoEsp": self.tipoEsp
                       }
        return dict_values


class MaterialObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp):
        global mueble_id_count
        global all_objects

        self.inventoryObject = InventoryObject("mat" + str(mueble_id_count), nombre, stack, precio, tipo, tipoEsp)
        mueble_id_count += 1

        all_objects.append(self.get_dict())

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()

        return base_dict


class MuebleObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, color, conjunto):
        global mueble_id_count
        global all_objects

        self.inventoryObject = InventoryObject("mu" + str(mueble_id_count), nombre, stack, precio, tipo, tipoEsp)
        mueble_id_count += 1

        self.color = color
        self.conjunto = conjunto

        all_objects.append(self.get_dict())

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["color"] = self.color
        base_dict["conjunto"] = self.conjunto

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


class PropObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, comestible):
        global prop_id_count
        global all_objects

        self.inventoryObject = InventoryObject("prop" + str(prop_id_count), nombre, stack, precio, tipo, tipoEsp)
        prop_id_count += 1

        self.comestible = comestible

        all_objects.append(self.get_dict())

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["comestible"] = self.comestible

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


class EquipableObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, lugar_eq):
        global prop_id_count
        global all_objects

        self.inventoryObject = InventoryObject("equi" + str(prop_id_count), nombre, stack, precio, tipo, tipoEsp)
        prop_id_count += 1

        self.lugar_eq = lugar_eq

        all_objects.append(self.get_dict())

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["lugar_eq"] = self.lugar_eq

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


class ColeccionableObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, estacion, tamanio, localizacion, rareza):
        global coleccionable_id_count
        global all_objects

        self.inventoryObject = InventoryObject("col" + str(coleccionable_id_count), nombre, stack, precio, tipo,
                                               tipoEsp)
        coleccionable_id_count += 1

        self.estacion = estacion
        self.tamanio = tamanio
        self.localizacion = localizacion
        self.rareza = rareza

        all_objects.append(self.get_dict())

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["estacion"] = self.estacion
        base_dict["tamanio"] = self.tamanio
        base_dict["localizacion"] = self.localizacion
        base_dict["rareza"] = self.rareza

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


# Globals
file_path = os.path.dirname(__file__) + "\\Json\\"

casas_path = file_path + "casas.json"
jugadores_path = file_path + "jugadores.json"
isla_path = file_path + "islas.json"
objeto_path = file_path + "objetos.json"

player_id_count = 0
mueble_id_count = 0
coleccionable_id_count = 0
material_id_count = 0
prop_id_count = 0
equipable_id_count = 0

personaje_id_count = 0

casa_id_count = 0

isla_id_count = 0

edificio_id_count = 0

vecino_id_count = 0

all_objects = []
all_casas = []
all_jugadores = []
all_vecinos = []


def get_random_color():
    random_value = random.randint(0, 5)
    color = ""
    if random_value == 0:
        color = "Blanco"
    elif random_value == 1:
        color = "Rojo"
    elif random_value == 2:
        color = "Amarillo"
    elif random_value == 3:
        color = "Azul"
    elif random_value == 4:
        color = "Marron"
    elif random_value == 5:
        color = "Rosa"

    return color


def get_adjective():
    adjectives = ["Genial", "Mediocre", "del Monton", "Comun", "Impresionante", "muy Cuqui", "Cuqui",
                  "Curioso", "Interesante", "sin Mas", "Correcto", "Atractivo", "Calido", "Precioso",
                  "Azulado", "de Campeones", "Elegante", "Estilizado", "Magnifico", "Chachi", "Medio Roto",
                  "Memorable", "que da que pensar", "Pijito", "Chismoso", "de Locos", "Perfecto", "Impecable",
                  "para cogerle carinio", "Especial", "muy Especial", "Vistosito", "Regu", "que no esta mal",
                  "un poco Hortera", "Hortera", "de Buen Gusto"]

    return adjectives[random.randint(0, len(adjectives) - 1)]


def get_material_dict_list(size):
    dict_list = []

    names = ["Piedra", "Pepita de Oro", "Madera", "Madera dura", "Madera blanda", "Hierro"]
    stacks = [10, 20, 100, 200, 300]
    precios = [10, 100, 150, 200, 250, 300, 500]

    for i in range(size):
        name = names[random.randint(0, len(names) - 1)]
        stack = stacks[random.randint(0, len(stacks) - 1)]
        precio = precios[random.randint(0, len(precios) - 1)]
        tipo = "Material"
        tipoEsp = name

        dict_list.append(MaterialObject(name + " " + get_adjective(), stack, precio, tipo, tipoEsp).get_dict())

    return dict_list


def get_prop_dict_list(size):
    dict_list = []

    names = ["Margarita", "Rosa", "Petunia", "Geranio",
             "Romero", "Lavanda", "Tomillo", "Ajenjo", "Hierbabuena",
             "Roble", "Manzano", "Abeto", "Pino", "Cipres", "Melocotonero",
             "Roca", "Amatista", "Caliza", "Marmol", "Arenisca", "Silex",
             "Naranja", "Manzana", "Uva", "Ciruela", "Tomate"
             ]
    stacks = [10, 20, 100, 200, 300]
    precios = [10, 100, 150, 200, 250, 300, 500]
    tipos = ["Flor", "Flor", "Flor", "Flor",
             "Arbusto", "Arbusto", "Arbusto", "Arbusto", "Arbusto",
             "Arbol", "Arbol", "Arbol", "Arbol", "Arbol", "Arbol",
             "Roca", "Roca", "Roca", "Roca", "Roca", "Roca",
             "Fruta", "Fruta", "Fruta", "Fruta", "Fruta"
             ]
    comestibles = [False, False, False, False,
                   False, False, False, False, False,
                   False, False, False, False, False, False,
                   False, False, False, False, False, False,
                   True, True, True, True, True]

    tipo = "Prop"
    for i in range(size):
        name_i = random.randint(0, len(names) - 1)

        name = names[name_i] + " " + get_adjective()
        stack = stacks[random.randint(0, len(stacks) - 1)]
        precio = precios[random.randint(0, len(precios) - 1)]
        tipoEsp = tipos[name_i]

        dict_list.append(PropObject(name, stack, precio, tipo, tipoEsp, comestibles[name_i]).get_dict())

    return dict_list


def get_equip_dict_list(size):
    dict_list = []

    names = ["Fedora", "Gorrita", "Sombrero de Ala", "Sombrero de paja", "Visera",
             "Blusa", "Jersey", "Camisa Hawaiana", "Chaleco", "Camisa",
             "Leggins", "Pantaloncito corto", "Kilt", "Chandal", "Falda", "Vaqueros",
             "Taconazo", "Zapatillas", "Sandalia", "Zuecos", "Chanclas", "Botas",
             "Red", "Pico", "Pala", "Cania", "Lupa"
             ]
    precios = [10, 100, 150, 200, 250, 300, 500, 1000, 2000, 2750, 5000]
    tipos = ["Ropa", "Ropa", "Ropa", "Ropa", "Ropa",
             "Ropa", "Ropa", "Ropa", "Ropa", "Ropa",
             "Ropa", "Ropa", "Ropa", "Ropa", "Ropa", "Ropa",
             "Ropa", "Ropa", "Ropa", "Ropa", "Ropa", "Ropa",
             "Herramienta", "Herramienta", "Herramienta", "Herramienta", "Herramienta"
             ]

    lugar_equips = ["Cabeza", "Cabeza", "Cabeza", "Cabeza", "Cabeza",
                    "Torso", "Torso", "Torso", "Torso", "Torso",
                    "Piernas", "Piernas", "Piernas", "Piernas", "Piernas", "Piernas",
                    "Pies", "Pies", "Pies", "Pies", "Pies", "Pies",
                    "Manos", "Manos", "Manos", "Manos", "Manos"]

    tipo = "Equipable"
    for i in range(size):
        name_i = random.randint(0, len(names) - 1)

        name = names[name_i] + " " + get_adjective()
        stack = 1
        precio = precios[random.randint(0, len(precios) - 1)]
        tipoEsp = tipos[name_i]
        lugar_equip = lugar_equips[name_i]

        dict_list.append(EquipableObject(name, stack, precio, tipo, tipoEsp, lugar_equip).get_dict())

    return dict_list


def get_col_dict_list(size):
    dict_list = []

    names = ["Craneo", "Amonites", "Hueso", "DinoHueso", "Trilobites",
             "Carpa", "Palometa", "Pez Sable", "Tiburon", "Mero",
             "BichoPalo", "Mariposa", "Hormiguita", "Escarabajo", "Escararriba"
             ]
    precios = [1000, 2000, 2750, 5000, 6000, 10000]
    tipos = ["Fosil", "Fosil", "Fosil", "Fosil", "Fosil",
             "Pez", "Pez", "Pez", "Pez", "Pez",
             "Insecto", "Insecto", "Insecto", "Insecto", "Insecto"
             ]

    localizations = ["Tierra", "Bajo tierra", "Tierra", "Bajo Tierra", "Bajo Tierra",
                     "Rio", "Mar", "Mar", "Mar", "Cascada",
                     "Estanque", "Valle", "Boca del Rio", "Colina", "Colina"]

    estaciones = ["Primavera", "Invierno", "Verano", "Otonio"]

    tipo = "Coleccionable"
    for i in range(size):
        name_i = random.randint(0, len(names) - 1)

        name = names[name_i] + " " + get_adjective()
        stack = 1
        precio = precios[random.randint(0, len(precios) - 1)]
        tipoEsp = tipos[name_i]
        estacion = estaciones[random.randint(0, len(estaciones) - 1)]
        tamanio = random.randint(1, 5)
        localization = localizations[name_i]
        rareza = random.randint(1, 10)

        dict_list.append(
            ColeccionableObject(name, stack, precio, tipo, tipoEsp, estacion, tamanio, localization, rareza).get_dict())

    return dict_list


def get_mueble_dict_list(size):
    dict_list = []

    names = ["Silla", "Mesa", "Mesita", "Armario", "Estanteria", "Cama"]
    precios = [10, 100, 150, 200, 250, 300, 500]
    tipo = "Mueble"
    conjuntos = ["Congelado", "Dorado", "Setas", "Flor de cerezo", "Bambu", "Mimbre", "Restaurante",
                 "Imperial",
                 "Flores", "Linda", "Mariana", "Veraniego", "Frutas", "Zodiaco", "Universitario"]

    stack = 1
    for i in range(size):
        name = names[random.randint(0, len(names) - 1)]
        precio = precios[random.randint(0, len(precios) - 1)]
        color = get_random_color()
        tipoEsp = name
        conjunto = conjuntos[random.randint(0, len(conjuntos) - 1)]

        dict_list.append(
            MuebleObject(name + " " + get_adjective(), stack, precio, tipo, tipoEsp, color, conjunto).get_dict())

    return dict_list


def write_file(file, values):
    file = open(file, "w")
    file.write(json.dumps(values))
    file.close()


def find_casa_by_id(casa_id):
    global all_casas
    casa_index = casa_id.replace('c', "")
    casa_index = int(casa_index)

    return all_casas[casa_index]


def get_casa():
    global casa_id_count
    global casas_list
    global all_casas

    casa_dict = {"_id": "c" + str(casa_id_count),
                 "colorFachada": get_random_color(),
                 "colorTejado": get_random_color(),

                 "inventarioCasa": (get_col_dict_list(random.randint(0, 5))
                                    + get_equip_dict_list(random.randint(0, 5))
                                    + get_prop_dict_list(random.randint(0, 5))
                                    + get_material_dict_list(random.randint(0, 5))
                                    + get_mueble_dict_list(random.randint(0, 5))
                                    )
                 }

    casa_id_count += 1
    all_casas.append(casa_dict)

    return casa_dict


def get_player():
    global jugadores_path
    global player_id_count
    global all_players
    global all_vecinos

    nombres = ["Pepito", "Juana", "Jennifer", "Stella"]
    name_id = player_id_count % len(nombres)

    bayas_list = [1000, 2000, 3000, 12000]

    player_id = "j" + str(player_id_count)
    player_id_count += 1
    nombre = nombres[name_id]

    casa = get_casa()

    bayas = bayas_list[random.randint(0, len(bayas_list) - 1)]
    millas = bayas_list[random.randint(0, len(bayas_list) - 1)]

    inventario = get_mueble_dict_list(random.randint(0, 3)) + \
                 get_equip_dict_list(random.randint(0, 10)) + \
                 get_col_dict_list(random.randint(0, 3)) + \
                 get_material_dict_list(random.randint(0, 3)) + \
                 get_prop_dict_list(random.randint(0, 3))

    vecinos = []

    jugador_dict = {
        "_id": player_id,
        "nombre": nombre,
        "casa": casa["_id"],
        "bayas": bayas,
        "millas": millas,

        "inventarioObjetos": inventario,
        "vecinos": vecinos
    }

    all_jugadores.append(jugador_dict)

    return jugador_dict


def write_islas(isla_count):
    global isla_path
    global edificio_id_count
    global all_casas
    global isla_id_count
    global personaje_id_count

    islas = []
    nombres = ["AlcorOn", "SouthPeru", "MostToLess", "TorriHoes", "WestMadriz"]
    hemisferios = ["N", "S"]

    fechas = ["10-5-2022", "9-5-2022", "11-5-2022", "12-5-2022"]
    horas = ["8:22:23", "9:22:23", "10:22:23", "11:22:23", "12:22:23", "13:22:23", "14:22:23"]
    climatologias = ["Nublado", "Soleado", "Tormenta", "Lluvia", "Nieve", "Muy Soleado", "Calima"]
    edificios = ["Ayuntamiento", "Museo", "Tienda", "Peluqueria", "Aerodromo"]
    personajes_names = ["Tom Nook", "Canela", "Arquimedes", "Pili y Mili", "Marilin", "Rodri y Rafa"]

    for i in range(isla_count):
        jugadores = []
        vecinos = []
        casas_de_isla = []
        objetos_de_isla = []

        edificios_dict_list = []

        edificios_ids = []
        for i in range(len(edificios)):
            dict = {
                "idEdificio": "ed" + str(edificio_id_count),
                "tipo": edificios[i],
                "inventarioEdificio": get_mueble_dict_list(random.randint(0, 5)) +
                                      get_col_dict_list(random.randint(0, 5)) +
                                      get_mueble_dict_list(random.randint(0, 5)) +
                                      get_prop_dict_list(random.randint(0, 5)) +
                                      get_material_dict_list(random.randint(0, 5)) +
                                      get_equip_dict_list(random.randint(0, 2))
            }

            edificios_ids.append(dict["idEdificio"])
            edificio_id_count += 1
            edificios_dict_list.append(dict)

        for i in range(random.randint(2, 8)):
            new_vecino = get_vecino()
            vecinos.append(new_vecino)

            casa_id = new_vecino["casa"]
            casas_de_isla.append(casa_id)

            # Find casa
            casa = find_casa_by_id(casa_id)
            objetos_de_isla += casa["inventarioCasa"]

        for i in range(random.randint(1, 3)):
            new_jugador = get_player()

            jugadores.append(new_jugador["_id"])

            casas_de_isla.append(new_jugador["casa"])

            casa = find_casa_by_id(new_jugador["casa"])

            objetos_de_isla.append(casa["inventarioCasa"])

            for j in range(len(vecinos)):
                all_vecinos_copy = all_vecinos.copy()

                for i in range(2, 5):
                    random_index = random.randint(0, len(all_vecinos_copy) - 1)
                    new_vecino = all_vecinos_copy.pop(random_index)

                    new_jugador["vecinos"].append({
                        "vecinoId": new_vecino["vecinoId"],
                        "amistad": random.randint(1, 10)

                    })

        personajes_dict = [
            {
                "idPersonaje": "pj" + str(personaje_id_count),
                "nombre": "Tom Nook",
                "edificioId": edificios_ids[0]
            },
            {
                "idPersonaje": "pj" + str(personaje_id_count + 1),
                "nombre": "Canela",
                "edificioId": edificios_ids[0]
            },
            {
                "idPersonaje": "pj" + str(personaje_id_count + 2),
                "nombre": "Arquimedes",
                "edificioId": edificios_ids[1]
            },
            {
                "idPersonaje": "pj" + str(personaje_id_count + 3),
                "nombre": "Pili y Mili",
                "edificioId": edificios_ids[2]
            },
            {
                "idPersonaje": "pj" + str(personaje_id_count + 4),
                "nombre": "Marilin",
                "edificioId": edificios_ids[3]
            },
            {
                "idPersonaje": "pj" + str(personaje_id_count + 5),
                "nombre": "Rodri y Rafa",
                "edificioId": edificios_ids[4]
            }
        ]

        personaje_id_count += 5

        isla_dict = {"_id": "is" + str(isla_id_count),
                     "jugadores": jugadores,
                     "nombre": nombres[i % len(nombres)],
                     "hemisferio": hemisferios[random.randint(0, len(hemisferios) - 1)],
                     "fecha": fechas[random.randint(0, len(fechas) - 1)],
                     "hora": horas[random.randint(0, len(fechas) - 1)],
                     "climatologia": climatologias[random.randint(0, len(climatologias) - 1)],
                     "edificios": edificios_dict_list,
                     "personajes": personajes_dict,
                     "inventarioIsla": objetos_de_isla,
                     "casas": casas_de_isla,
                     "vecinos": vecinos
                     }
        islas.append(isla_dict)
        isla_id_count += 1

    write_file(isla_path, {"Islas": islas})


def get_vecino():
    global vecino_id_count
    global all_vecinos

    names = ["Paco", "Joshua", "Patri", "Marcelyn", "Apollo", "Steacy", "Carlos", "Queque", "Ariel",
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

    personalidades = ["Atletico", "Esnob", "Grunion", "Perezoso", "Alegre", "Dulce", "Presumida", "Normal"]

    casa = get_casa()

    name_id = vecino_id_count
    if vecino_id_count >= len(names):
        name_id = name_id % len(names)

        print("Care: Names are repeated!")

    vecino_dict = {
        "vecinoId": "vec" + str(name_id),
        "nombre": names[vecino_id_count],
        "personalidad": personalidades[random.randint(0, len(personalidades) - 1)],
        "casa": casa["_id"]
    }
    vecino_id_count += 1

    all_vecinos.append(vecino_dict)

    return vecino_dict


write_islas(3)

write_file(objeto_path, {"Objetos": all_objects})
write_file(casas_path, {"Casas": all_casas})
write_file(jugadores_path, {"Jugadores": all_jugadores})
