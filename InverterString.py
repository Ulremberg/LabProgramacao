entrada = input()
invertendoPalavra = ''

for i in range(len(entrada) - 1, -1, -1):
    invertendoPalavra += entrada[i]
print(invertendoPalavra)