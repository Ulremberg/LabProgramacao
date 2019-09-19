import math

numero = int(input("Digite o numero : \n"))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" * ")
    count -= 1
print("1 = {} ". format(fatorial))