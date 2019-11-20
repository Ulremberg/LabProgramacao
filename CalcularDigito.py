def validar(cpf):
    #cpf = input().strip().upper()
    valido = "VALIDO"
    invalido = "INVALIDO"
    digito = list(cpf)
    g1 = max(digito[0], digito[1], digito[2])
    g2 = max(digito[4], digito[5], digito[6])
    g3 = max(digito[8], digito[9], digito[10])
    dv = (int(g1)+int(g2)+int(g3))%10
    if dv == int(digito[12]):
        return valido
    else:
        return invalido

entrada = input().strip().upper()
while entrada != "FIM":
    print(validar(entrada))
    entrada = input().strip().upper()

