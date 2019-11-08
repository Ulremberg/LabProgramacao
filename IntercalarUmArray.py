entrada = int(input())
matriz = []
matriz_intercalar = []

for x in range(entrada):
    matriz.append(input())

for x in range(entrada):
    matriz_intercalar.append(input())

for i in range(entrada):
    print(matriz[i])
    print(matriz_intercalar[i])