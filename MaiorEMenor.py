# coding: utf-8

a = int(input("Entre com o primeiro valor: \n"))
b = int(input("Entre com o segundo valor: \n"))
c = int(input("Entre com o terceiro valor: \n"))

if(a > b and b > c):
    print('{} > {} > {}'.format(a,b,c))
elif(a > b and c > b):
    print('{} > {} > {}'.format(a,c,b))
elif(b > a and a > c):
    print('{} > {} > {}'.format(b,a,c))
elif(b > a and c > a):
    print('{} > {} > {}'.format(b,c,a))
elif(c > a and a > b):
    print('{} > {} > {}'.format(c,a,b))
elif(c > b and b > a):
    print('{} > {} > {}'.format(c,b,a))