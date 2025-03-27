import json
def guardarJSON(datos, nombre):
    with open(nombre, "w") as file:
        json.dump(datos, file, indent=4)

def cargarJSON(nombre):
    try:
        with open(nombre, "r") as fichero:
            return json.load(fichero)
    except FileNotFoundError:
        return {}