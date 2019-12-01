pokemonRed = 'Pokemon do Red: '
pokemonBlue = 'Pokemon do Blue: '
dadosPokemonRed = {}
dadosPokemonBlue = {}
allPokemonRed = []
allPokemonBlue = []
nomeRed = []
nomeBlue = []
idRed = []
idPokemonRed = []
idBlue = []
idPokemonBlue = []
atkRed = []
atkBlue = []
lifeRed = []
lifeBlue = []

cadastrototal = {}
count = 0
nomePokemon = []
idPokemon = []
atkPokemon = []
lifePokemon = []
while count != 12:
    cadastrototal["Nome"] = input()
    nomePokemon.append(cadastrototal["Nome"])
    cadastrototal["Id"] = int(input())
    idPokemon.append(cadastrototal["Id"])
    cadastrototal["Ataque"] = int(input())
    atkPokemon.append(cadastrototal["Ataque"])
    cadastrototal["Vida"] = int(input())
    lifePokemon.append(cadastrototal["Vida"])
    if(count < 6):
        allPokemonRed.append(cadastrototal)
    if(count >= 6):
        allPokemonBlue.append(cadastrototal)
    cadastrototal = {}
    count = count + 1

# for i in range(6):
#     dadosPokemonRed["Nome"] = input()
#     nomeRed.append(dadosPokemonRed["Nome"])
#     dadosPokemonRed["Id"] = int(input())
#     idPokemonRed.append(dadosPokemonRed["Id"])
#     dadosPokemonRed["Ataque"] = int(input())
#     atkRed.append(dadosPokemonRed["Ataque"])
#     dadosPokemonRed["Vida"] = int(input())
#     lifeRed.append(dadosPokemonRed["Vida"])
#     allPokemonRed.append(dadosPokemonRed)
# for x in range(6):
#     dadosPokemonBlue["Nome"] = input()
#     nomeBlue.append(dadosPokemonBlue["Nome"])
#     dadosPokemonBlue["Id"] = int(input())
#     idPokemonBlue.append(dadosPokemonBlue["Id"])
#     dadosPokemonBlue["Ataque"] = int(input())
#     atkBlue.append(dadosPokemonBlue["Ataque"])
#     dadosPokemonBlue["Vida"] = int(input())
#     lifeBlue.append(dadosPokemonBlue["Vida"])
#     allPokemonBlue.append(dadosPokemonBlue)
# print(allPokemonRed)
# print(allPokemonBlue)
for i in range(len(atkPokemon)):
    redEscolhe = max(atkPokemon[0], atkPokemon[1], atkPokemon[2], atkPokemon[3], atkPokemon[4], atkPokemon[5])
    for x in range(len(allPokemonRed)):
        for y in range(len(allPokemonRed[x])):
            if (redEscolhe == allPokemonRed[x]["Ataque"]):
                idRed.append(allPokemonRed[x]["Id"])
                pokemonRedFinal = min(idRed)
                if (pokemonRedFinal == allPokemonRed[x]["Id"] and redEscolhe == allPokemonRed[x]["Ataque"]):
                    nomePokemonEscolhidoFinalRed = allPokemonRed[x]["Nome"]
                    vidaPokemonEscolhidoFinalRed = allPokemonRed[x]["Vida"]

for i in range(len(atkPokemon)):
    blueEscolhe = max(atkPokemon[6], atkPokemon[7], atkPokemon[8], atkPokemon[9], atkPokemon[10], atkPokemon[11])
    for x in range(len(allPokemonBlue)):
        for y in range(len(allPokemonBlue[x])):
            if (blueEscolhe == allPokemonBlue[x]["Ataque"]):
                idBlue.append(allPokemonBlue[x]["Id"])
                pokemonBlueFinal = min(idBlue)
                if (pokemonBlueFinal == allPokemonBlue[x]["Id"] and blueEscolhe == allPokemonBlue[x]["Ataque"]):
                    nomePokemonEscolhidoFinalBlue = allPokemonBlue[x]["Nome"]
                    vidaPokemonEscolhidoFinalBlue = allPokemonBlue[x]["Vida"]

print("{}{}".format(pokemonRed, nomePokemonEscolhidoFinalRed))
print("{}{}".format(pokemonBlue, nomePokemonEscolhidoFinalBlue))
count_vidaRed = 0
count_vidaBlue = 0
while(vidaPokemonEscolhidoFinalRed > 0):
    vidaPokemonEscolhidoFinalRed = vidaPokemonEscolhidoFinalRed - blueEscolhe
    count_vidaRed = count_vidaRed + 1
while(vidaPokemonEscolhidoFinalBlue > 0):
    vidaPokemonEscolhidoFinalBlue = vidaPokemonEscolhidoFinalBlue - redEscolhe
    count_vidaBlue = count_vidaBlue + 1

if(count_vidaRed < count_vidaBlue):
    print('Vencedor: Blue')
elif(count_vidaBlue < count_vidaRed):
    print("Vencedor: Red")
elif(count_vidaBlue == count_vidaRed):
    print("Empate")