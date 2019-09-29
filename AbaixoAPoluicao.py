entrada = []
casasMultadas = 0
multaArrecadada = 0
numeroCarros = 0

while (numeroCarros != 999):
    numeroCarros = int(input())
    if (numeroCarros == 999):
        break
    if (numeroCarros > 2):
        quantidade = numeroCarros - 2
        multaArrecadada = multaArrecadada + (quantidade * 12.89)
        casasMultadas += 1
        entrada.append(numeroCarros)

    elif(numeroCarros <=2):
            casasMultadas = 0
            multaArrecadada = 0

print(multaArrecadada)
print(casasMultadas)
