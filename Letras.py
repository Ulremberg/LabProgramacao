letra = input()
palavra = input()

cont = palavra.count(letra)

calculo = cont/ len(palavra) * 100

print("{:.2f}".format(calculo))