a = input().split()
total = int(a[0])
resolvidos = int(a[1])

percent_cump = 100 * (resolvidos / total)

if (percent_cump < 20):
    chance = 4.4
    conceito = 'Pessimo'

elif (percent_cump < 40):
    chance = 31.65
    conceito = 'Ruim'
elif (percent_cump < 60):
    chance = 56.82
    conceito = 'Bom'
elif (percent_cump < 80):
    chance = 80.0
    conceito = 'Muito Bom'
else:
    chance = 94.0
    conceito = 'Excelente'

print('{:.2f}% {:.2f}% {}'.format(percent_cump, chance, conceito))