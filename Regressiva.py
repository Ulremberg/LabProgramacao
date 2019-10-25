def funcao(numero):
    for i in range(numero, -1, -1):
        for x in range(i):
            if x == i - 1:
                print(i)
            else:
                print(i, end='-')


entrada = int(input())
funcao(entrada)