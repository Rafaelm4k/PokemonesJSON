from CargarJSONS import cargarJSON,guardarJSON
pokedex = cargarJSON("pokedex.json")
def setGeneralInfo(pokemon):
    infoGeneral = ["nombre","genero","nivel"]
    for info in infoGeneral:
        pokemon[info] = input(f"Dime su {info} : ")

def setGeneralStats(pokemon):
    Infostats = ["ps","ataque","ataqueEspecial","velocidad","defensa","defensaEspecial"]
    stats = {}
    for stat in Infostats:
        stats[stat] = input(f"Dime su {stat} : ")
    pokemon["stats"] = stats

def setStroke(pokemon):
    infoAtaque = ["nombreAtaque","tipo","damage","categoria","pp"]
    numAtaques = int(input("Cuantos ataques tiene el pokemon? 1/4 : "))
    ataques = []
    for i in range(numAtaques):
        ataque = {}
        for info in infoAtaque:
            ataque[info] = input(f"Dime su {info} : ")
        ataques.append(ataque)
    pokemon["ataques"] = ataques

try:
    pokemons = pokedex["pokemons"]
except KeyError:
    pokedex["pokemons"] = []
    pokemons = pokedex["pokemons"]

continuar = True
while continuar:
    pokemon = {}
    setGeneralInfo(pokemon)
    setGeneralStats(pokemon)
    setStroke(pokemon)
    pokemons.append(pokemon)
    if input("Desea Salir? s/n : ").lower() != "s":
        continuar = False

pokedex["pokemons"] = pokemons
guardarJSON(pokemons,"pokedex.json")