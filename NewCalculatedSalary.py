salario = int(input())

novosalario = None
if (salario >= 500):
    novosalario = ((salario * 0.1) + salario)

elif (salario > 300 and salario < 500):
    novosalario = ((salario * 0.07) + salario)

elif (salario < 300):
    novosalario = ((salario * 0.03) + salario)

if novosalario:
    print('{}'.format(novosalario))
