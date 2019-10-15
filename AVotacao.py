# Sua missão é fazer um programa que ajude a computar todos os votos e decidir qual dos dois animes foi o mais votado.
# Existem apenas dois tipos de votos, o "c" que significa que a pessoa votou em Cavaleiros do Zodíaco e "p" que significa que a pessoa
# votou em Pokémon.
#
# OBS: Nunca haverá empate, sempre um dos dois vai ser o mais votado

# Exemplo:
# #
# # 4 ppcp
# #
# # Nesse caso, 4 pessoas de uma determinada turma participaram desta votação,
# # com 3 pessoas votando em Pokémon e apenas uma votando em Cavaleiros do Zodíaco.

voto = []
cavaleiro = 0
pokemon = 0

turma = int(input())

for i in range(turma):
    voto.append(input().split())

for x in range(len(turma)):
    entrada = list(voto[x][1])
    cavaleiro = cavaleiro + entrada.count('c')
    pokemon = pokemon + entrada.count('p')

if (cavaleiro > pokemon):
    print('Cavaleiros do zodiaco ganhou e teve o total de {} votos'.format(cavaleiro))
else:
    print('Pokemon ganhou e teve o total de {} votos'.format(pokemon))

