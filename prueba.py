pokedex = cargarJSON("pokedex.json")

def darInformacionGeneral(pokemon):
    infoGeneral = ["nombre", "genero", "nivel"]
    for info in infoGeneral:
        pokemon[info] = input(f"Dime su {info}: ")

def darStats(pokemon):
    infoStats = ["ps", "ataque", "ataqueEspecial", "velocidad", "defensa", "defensaEspecial"]
    stats = {}
    for stat in infoStats:
        stats[stat] = input(f"Dime su {stat}: ")
    pokemon["stats"] = stats

def darAtaques(pokemon):
    infoAtaque = ["nombreAtaque", "tipo", "damage", "categoria", "pp"]
    numAtaques = int(input("¿Cuántos ataques tiene? (1-4): "))
    ataques = []
    for i in range(numAtaques):
        ataque = {}
        for info in infoAtaque:
            ataque[info] = input(f"Dime su {info}: ")
        ataques.append(ataque)
    pokemon["ataques"] = ataques

continuar = True
try:
    pokemons = pokedex["pokemons"]
except KeyError:
    pokedex["pokemons"] = []
    pokemons = pokedex["pokemons"]

while continuar:
    pokemon = {}
    darInformacionGeneral(pokemon)
    darStats(pokemon)
    darAtaques(pokemon)
    pokemons.append(pokemon)
    if input("¿Continuar? s/n").lower() != "s":
        continuar = False

pokedex["pokemons"] = pokemons
guardarJSON(pokedex, "pokedex.json")