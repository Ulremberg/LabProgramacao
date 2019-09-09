#Escrever um algoritmo que lê 5 valores para "a",
# um de cada vez, e conta quantos destes são negativos, escrevendo esta informação.

#valor = int(input())

valores = 5

conte = 0

for i in range(0,5):
    valor = float(input('Digite um valor:\n'))
    if(valor < 0):
        conte += 1
    else:
        conte == conte

print('Foram digitados {} numeros negativos'.format(conte))

