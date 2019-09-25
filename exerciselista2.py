nota = []
for i in range(0,4):
    nota.append(int(input('Digite um numero\n')))

not1 = nota[0]
not2 = nota[1]
not3 = nota[2]
not4 = nota[3]

media = ((not1 + not2 + not3 + not4) / 4)

print('As notas foram {}, {} , {} , {} e a media foi {}'.format(not1, not2, not3, not4, media))
