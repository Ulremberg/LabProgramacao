# Faça um programa que leia um número indeterminado de
# valores, correspondentes a notas. Após esta entrada de dados,
# faça:
#  Mostre a quantidade de valores que foram lidos;
#  Exiba todos os valores na ordem em que foram informados;
#  Exiba todos os valores na ordem inversa à que foram informados, um
# abaixo do outro;
#  Calcule e mostre a soma dos valores;
#  Calcule e mostre a média dos valores;
#  Calcule e mostre a quantidade de valores acima da média calculada;
#  Calcule e mostre a quantidade de valores abaixo de sete;
#  Encerre o programa com uma mensagem

nota = []
n = int(input('Determine o número de notas a ser digitado:\n'))
for i in range(0, n):
    nota.append(float(input("Digite a nota:\n")))

print('A quantidade de notas entradas foi: {}'.format(n))

print('A ordem das notas informadas foi: {}'.format(nota))

print('A ordem inversa das notas informadas foi: {}'.format(reversed(nota)))

soma = sum(nota)
print('A soma dos valores foi: {}'.format(soma))

media = sum(nota) / n
print('A média das notas foi: {}'.format(media))

acimaDaMedia = 0
if(nota > media):
    acimaDaMedia = acimaDaMedia + 1
    print('A quantidade de nota acima da média foi: {}'.format(acimaDaMedia))
else:
    acimaDaMedia = acimaDaMedia
    print('A quantidade de nota acima da média foi: {}'.format(acimaDaMedia))

