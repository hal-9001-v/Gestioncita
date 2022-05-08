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

        self.inventoryObject = InventoryObject("mu" + str(mueble_id_count), nombre, stack, precio, tipo, tipoEsp)
        mueble_id_count += 1

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()

        return base_dict


class MuebleObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, color, conjunto):
        global mueble_id_count

        self.inventoryObject = InventoryObject("mu" + str(mueble_id_count), nombre, stack, precio, tipo, tipoEsp)
        mueble_id_count += 1

        self.color = color
        self.conjunto = conjunto

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
        self.inventoryObject = InventoryObject("prop" + str(prop_id_count), nombre, stack, precio, tipo, tipoEsp)
        prop_id_count += 1

        self.comestible = comestible

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["comestible"] = self.comestible

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


class EquipableObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, lugar_eq):
        global prop_id_count

        self.inventoryObject = InventoryObject("equi" + str(prop_id_count), nombre, stack, precio, tipo, tipoEsp)
        prop_id_count += 1

        self.lugar_eq = lugar_eq

    def get_dict(self):
        base_dict = self.inventoryObject.get_dict()
        base_dict["lugar_eq"] = self.lugar_eq

        return base_dict

    def get_json(self):
        return json.dumps(self.get_dict())


class ColeccionableObject:
    def __init__(self, nombre, stack, precio, tipo, tipoEsp, estacion, tamanio, localizacion, rareza):
        global coleccionable_id_count

        self.inventoryObject = InventoryObject("col" + str(coleccionable_id_count), nombre, stack, precio, tipo,
                                               tipoEsp)
        coleccionable_id_count += 1

        self.estacion = estacion
        self.tamanio = tamanio
        self.localizacion = localizacion
        self.rareza = rareza

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

test_path = file_path + "text.json"

mueble_id_count = 0
coleccionable_id_count = 0
material_id_count = 0
prop_id_count = 0
equipable_id_count = 0

casa_id_count = 0


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
                  "Memorable", "que da que pensar"]

    return adjectives[random.randint(0, len(adjectives) - 1)]


def get_material_dict_list(size):
    dict_list = []

    names = ["Piedra", "Cemento", "Madera", "Ceramica", "Metal", "Barro"]
    stacks = [10, 20, 100, 200, 300]
    precios = [10, 100, 150, 200, 250, 300, 500]

    for i in range(size):
        name = names[random.randint(0, len(names) - 1)] + " " + get_adjective()
        stack = stacks[random.randint(0, len(stacks) - 1)]
        precio = precios[random.randint(0, len(precios) - 1)]
        tipo = "Material"
        tipoEsp = name

        dict_list.append(MaterialObject(name, stack, precio, tipo, tipoEsp).get_dict())

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

        dict_list.append(ColeccionableObject(name, stack, precio, tipo, tipoEsp, estacion, tamanio, localization, rareza).get_dict())

    return dict_list


def write_file(file, values):
    file = open(file, "w")
    file.write(json.dumps(values))
    file.close()


def write_casas(casa_count):
    for i in range(casa_count):
        casa_dict = [{"_id": "c" + str(i),
                      "colorFachada": get_random_color(),
                      "colorTejado": get_random_color(),

                      "inventarioCasa": [

                      ]
                      }]


val = {"Caquita": get_col_dict_list(100)}
write_file(test_path, val)
