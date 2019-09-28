# Zelda e seus amigos tiveram uma brilhante ideia durante as aulas da monitoria
# da cadeira de introdução a programação: que tal fazer um programa que,
# dado um número n (1 <= n <= 40) printa na tela os numeros de 1 até o número da iteração atual,
# sendo que serão feitas n iterações, como demonstrado no exemplo a seguir:
#
# Supondo para n = 5:
#
# (primeira iteração):  1
# (segunda iteração): 1 2
# (terceira iteração):   1 2 3
# (quarta iteração):     1 2 3 4
# (quinta iteração):     1 2 3 4 5

entrada = int(input())
for i in range(1, entrada + 1):
    for num in range(1, i + 1):
        if num == i:
            print(num)
        else:
            print(num, end=' ')
