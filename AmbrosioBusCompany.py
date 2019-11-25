#class onibus:

arr = []
idade = []
dados_passageiro = {}
while True:
    dados_passageiro["numero_passageiros"] = int(input())
    if dados_passageiro["numero_passageiros"] == -1:
        break
    else:
        dados_passageiro["Data"] = input()
        dados_passageiro["origem"] = input()
        dados_passageiro["destino"] = input()
        dados_passageiro["horario"] = input()
        dados_passageiro["Poltrona"] = int(input())
        dados_passageiro["idade"] = int(input())
        idade.append(dados_passageiro["idade"])
        dados_passageiro["nome"] = input()
        arr.append(dados_passageiro)
        dados_passageiro = {}
for dados_passageiro in arr:
    if dados_passageiro["idade"] > (sum(idade)/len(idade)) and dados_passageiro["Poltrona"] % 2 == 0:
        print('{}'.format(dados_passageiro["nome"]))