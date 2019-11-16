entrada = list(map(float, input().split()))
def reduz(entrada):
    primero_valor = entrada[0]
    segundo_valor = entrada[1]
    primero_valor = primero_valor - segundo_valor
    print('{:.2f} {:.2f}'.format(primero_valor, segundo_valor))

reduz(entrada)