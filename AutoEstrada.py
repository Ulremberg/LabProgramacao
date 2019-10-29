comprimento = int(input())
pista = input()
vetor = []
paineis = {
    "P":2,
    "C":2,
    "A":1,
    "D":0}
qtd_paineis = 0

for i in pista:
    vetor.append(i)
for x in vetor:
    qtd_paineis = qtd_paineis + paineis[x]
print(qtd_paineis)