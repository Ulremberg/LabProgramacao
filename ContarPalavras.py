entrada = input()
palavras = entrada.split(" ")
for i in palavras:
    if len(i) == 0:
        while i in palavras:
            palavras.remove(i)
print(len(palavras))
