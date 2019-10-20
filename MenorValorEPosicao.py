qtd_numeros = int(input())
numeros = input().split()

array = []

for i in numeros:
    a = int(i)
    array.append(a)

if (len(array) == qtd_numeros):
    print("Menor valor:", min(array))
    print("Posicao:", array.index(min(array)))
else:
    print("Programa finalizado")
