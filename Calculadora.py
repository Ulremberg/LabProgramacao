digito1 = float(input())
digito2 = float(input())
operacao = input()

while (operacao != '&'):
    if (operacao == '-'):
        digito1 -= digito2
        print('{:.3f}'.format(digito1))
    elif (operacao == '+'):
        digito1 += digito2
        print('{:.3f}'.format(digito1))
    elif (operacao == '*'):
        digito1 *= digito2
        print('{:.3f}'.format(digito1))
    elif (operacao == '/'):
        if (digito2 == 0):
            print("operacao nao pode ser realizada")
        else:
            digito1 /= digito2
            print('{:.3f}'.format(digito1))
    digito2 = float(input())
    operacao = input()
