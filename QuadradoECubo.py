linhas = int(input())
if(1 <= linhas <= 1000):
    for i in range(1, linhas + 1):
        numero = i
        cubo = i**3
        quadrado = i ** 2
        print('{} {} {}'.format(numero, quadrado, cubo))