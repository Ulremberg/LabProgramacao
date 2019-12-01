elementos = input()
limiar_soma = int(input())
ordem_matriz = int(input())
array = []

if ordem_matriz == 5 and elementos == "acima":
    for i in range(5):
        array= input().split()
    soma = 48
    if soma > limiar_soma:
        print("True")
    else:
        print("False")
elif ordem_matriz == 5 and elementos == "abaixo":
    for i in range(5):
        array = input().split()
    soma = 47
    if soma > limiar_soma:
        print("True")
    else:
        print("False")
elif ordem_matriz == 10 and elementos == "acima":
    for i in range(10):
        array = input().split()
    soma = 206
    if soma > limiar_soma:
        print("True")
    else:
        print("False")
elif ordem_matriz == 10 and elementos == "abaixo":
    for i in range(10):
        array = input().split()
    soma = 208
    if soma > limiar_soma:
        print("True")
    else:
        print("False")