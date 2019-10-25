r1 = float(input())
r2 = float(input())
calc1 = 3.14 * (r1 ** 2)
calc2 = 3.14 * (r2 ** 2)

if(calc1 > calc2):
    print('Primeiro circulo')
elif(calc2 > calc1):
    print('Segundo circulo')
elif(calc1 == calc2):
    print('Iguais')