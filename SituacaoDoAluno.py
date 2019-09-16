Media, nAulas, nFaltas = input().split(" ")

Media = float(Media)
nAulas = int(nAulas)
nFaltas = int(nFaltas)

frequencia = (((nAulas - nFaltas) / nAulas) * 100)

if ((frequencia >= 75 and Media >= 5) or (frequencia >= 50 and Media >= 7)):
    print("Aprovado")
else:
    print("Reprovado")
