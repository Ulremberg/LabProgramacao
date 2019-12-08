def converter(hora):
    meianoite = 00
    if hora > 12 and hora < 24:
        contador = 0
        for x in range(hora):
            if x >= 12:
                contador += 1
        return contador
    elif hora == 24:
        return meianoite
    else:
        return hora


controle = "sim"
while controle != "nao":
    hora = int(input("Digite a hora a ser convertida: "))
    minuto = int(input("Digite o minuto: "))
    print("Convertido: %i:%i" % (converter(hora), minuto))
    controle = input("Continuar? sim/ nao: ")
print("Até a próxima")
