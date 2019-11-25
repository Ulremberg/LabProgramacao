qtd_monstros = int(input())
monstros = []
dados = {}
for x in range(qtd_monstros):
    dados = {}
    dados["Nome"] = input()
    dados["ID"] = int(input())
    dados["Level"] = int(input())
    dados["Vida"] = int(input())
    dados["Ataque"] = int(input())
    dados["Defesa"] = int(input())
    monstros.append(dados)
for i in monstros:
    print("Nome:{}".format(i["Nome"]))
    print("ID:{}".format(i["ID"]))
    print("Level:{}".format(i["Level"]))
    print("Vida:{}".format(i["Vida"]))
    print("Ataque:{}".format(i["Ataque"]))
    print("Defesa:{}".format(i["Defesa"]))