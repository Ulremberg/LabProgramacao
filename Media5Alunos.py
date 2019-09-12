# coding: utf-8

media = 0

for nota in range(5):
    nota = float(input("Digite a nota:\n"))
    if (nota >= 0):
        media += nota

    else:
        return nota


# print(media)
print(media / 5)
