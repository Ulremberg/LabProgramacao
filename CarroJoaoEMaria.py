entrada = input()

if(entrada == 'n'or entrada == 'N'):
    print('zero')

if(entrada == 's'or entrada == 'S'):
    anoCarro = []
    velocidadeCarro = []
    while(entrada == 's' or entrada == 'S'):
        ano = int(input())
        velocidade = float(input())
        entrada = input()
        anoCarro.append(ano)
        velocidadeCarro.append(velocidade)
        if(entrada == 'N' or entrada == 'n'):
            print('{:.2f}'.format(max(velocidadeCarro)))
            print(max(anoCarro))
            vmed= (sum(velocidadeCarro)) / (len(velocidadeCarro))
            print('{:.2f}'.format(vmed))
            break