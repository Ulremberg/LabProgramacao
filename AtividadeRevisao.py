entrada1 = 0.0
entrada2 = 0.0
print('Bem vindo ao programada de soma. Digite dois valores e quando desejar finalizar o programa digite -1')
while(entrada1 != -1 or entrada2 != -1):
    entrada1 = float(input('Digite um valor inteiro:\n'))
    entrada2 = float(input('Digite um valor inteiro:\n'))
    print('A soma foi: {:.2f}'.format(entrada1 + entrada2))