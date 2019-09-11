# coding: utf-8
nota = None
while nota < 0 or nota > 10:
    if (nota < 0 or nota > 10):
        nota = float(input("Digite uma nota de 0 a 10: "))
    else:
        print("Nota inválida, digite apenas uma nota de 0 a 10.")

print("Nota: %.1f" % nota)
