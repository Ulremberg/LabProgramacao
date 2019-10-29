entrada1 = input().split()
entrada2 = input().split()

valor1 = int(entrada1[1]) * float(entrada1[2])
valor2 = int(entrada2[1]) * float(entrada2[2])

print('VALOR A PAGAR: R$ {:.2f}'.format(valor1 + valor2))