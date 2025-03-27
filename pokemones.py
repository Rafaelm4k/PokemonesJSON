from CargarJSONS import cargarJSON,guardarJSON

pokemon = {}
def PokemonTipo():
    if int(input("Cuantos tipos tiene el pokemon ? ")) == 1 :
        pokemon["tipo"] = [input("Que tipo es : ")]
    else:
        pokemon["tipo"] = [input("dime el tipo 1: ") , input("dime el tipo 2: ") ]

def PokemonStats():
    pokemon["stats"] = {
        "vida" : int(input("Ingrese cantidad de vida : ")),
        "velocidad": int(input("Ingresa la velocidad : ")),
        "ataque" : int(input("Ingresa Ataque : ")),
        "ataqueEspecial" : int(input("Ingresa ataque Especial : ")),
        "defensa" : int(input("Ingresa defensa : ")),
        "defensaEspecial" : int(input("Ingresa Defensa Especial : "))
    }

def PokemonAtaques():
    ataque = {
        "nombreAtaque" : input("Nombre del ataque : "),
        "tipo" : input("Que tipo es el ataque : "),
        "dano" : int(input("Ingresa la cantidad de daño : ")),
        "categoria" : input("El ataque es fis,est,esp? : " ),
        "pp" : int(input("Cuantos pp tiene el ataque : "))
    }
    return ataque
    
continuar = True
while continuar:
    pokemon["numpokedex"] = int(input("Numero de Pokemon : "))
    pokemon["nombre"]= input("Nombre del pokemon : ")
    PokemonTipo()
    PokemonStats()
    pokemon["ataques"] = []
    for i in range(4):
        print(f"Ingresando el ataque Numero {i+1}")
        pokemon["ataques"].append(PokemonAtaques())
    guardarJSON(pokemon,"pokemones.json")
    guardar = cargarJSON("pokemones.json")
    print(guardar)    

    if input("Desea Salir? s/n : ").lower() == "s":
        continuar = False