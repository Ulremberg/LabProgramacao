quantidade = int(input())
cidade = input()
qtdQuartos = int(input())

if (cidade.lower() == "pipa"):
    if (qtdQuartos == 2):
        valorTotal = (quantidade * 75) + 600
        valorUnit = valorTotal / quantidade
    else:
        valorTotal = (quantidade * 75) + 900
        valorUnit = valorTotal / quantidade
else:
    if (qtdQuartos == 3):
        valorTotal = (quantidade * 60) + 950
        valorUnit = valorTotal / quantidade
    else:
        valorTotal = (quantidade * 60) + 1120
        valorUnit = valorTotal / quantidade


print('{:.2f}'.format(valorTotal))
print('{:.2f}'.format(valorUnit))