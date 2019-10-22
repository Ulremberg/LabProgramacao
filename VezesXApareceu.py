numeros = []
count = 0
for x in range(10):
    numeros.append(int(input()))
buscado = int(input())
for num in numeros:
    if num == buscado:
        count = count + 1
print('{}'.format(count))