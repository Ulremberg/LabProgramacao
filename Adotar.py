# A Idade do Adotante
# #
# # Se o adotante é irmão ou ascendente
# #
# # Se é Adoção Conjunta
# #
# # Adotantes são casados ou união estável
# #
# # Idade do Adotando
# #
# # Pais Desconhecidos ou Adotando Destituído do Poder Familiar?
# #
# # Consentimento dos pais quando não desconhecidos
# #
# # Consentimento do adotando maior de doze anos de idade

idadeAdotante = int(input())
if(idadeAdotante < 18):
    idadeAdotante
else:
    ascendente = input()
    adocacaoConjunta = input()
    casado = input()
    idadeAdotando = int(input())
    paisDesconhecido = input()
    consetimento = input()
    consetimentoMaior = input()

if (idadeAdotante < 18):
    print("Não pode adotar")
elif (ascendente == "S"):
    print("Não pode adotar")
elif (
        idadeAdotante > 17 and ascendente == "N" and adocacaoConjunta == "N" and casado == "N" and idadeAdotando < 12 and paisDesconhecido == "N" and consetimento == "S" and consetimentoMaior == "N"):
    print("Pode adotar")
elif(idadeAdotante - idadeAdotando < 16):
    print("Não pode adotar")
elif(idadeAdotando > 12 and consetimentoMaior == "N"):
    print("Não pode adotar")