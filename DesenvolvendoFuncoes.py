# Um ano é bissexto se ele satisfaz as seguintes condições:
#
# É divisível por 4 e,
# Não é divisível por 100 ou é divisível por 400.
# A sua tarefa é construir uma solução com três funções (3): contaDigitos, ehBissexto e Mensagem.

# Para cada valor da entrada uma mensagem deve ser exibida.
#
# Se o valor é um ano bissexto mas for um ano anterior ao ano atual: O ano xxxx foi bissexto
# Se o valor é um ano bissexto mas for um ano posterior ao ano atual: O ano xxxx serah bissexto
# Se o valor não é um ano bissexto: O ano xxxx NAO eh bissexto
# Se o número não é um ano de 4 dígitos: Ano invalido

# valido = lambda x: "Valido"
invalido = "Ano invalido"
# antes_atual = lambda anterior: 2019 - anterior
def digitos(entrada):
    maior = 0
    menor = 0
    for i in range(len(entrada)):
        if int(entrada[i]) < 1000:
            menor = menor + 1
        else:
            maior = maior + 1
    if menor > 0:
        return menor
    else:
        return maior
def bissexto(entrada):
    for i in range(len(entrada)):
        if entrada[i] % 100 != 0 and entrada[i]% 4 == 0 or entrada[i] % 400 == 0:
            return "ehbissexto"
        else:
            return "naoeh"
def mensagem(entrada):
    for i in range(len(entrada)):
        if entrada[i] < 1000:
            print('Ano invalido')
        elif entrada[i] < 2019 and entrada[i] % 100 != 0 and entrada[i] % 4 == 0 or entrada[i] % 400 == 0:
            print('O ano {} foi bissexto'.format(entrada[i]))
        elif entrada[i] > 2019 and entrada[i] % 100 != 0 and entrada[i] % 4 == 0 or entrada[i] % 400 == 0:
            print('O ano {} serah bissexto'.format(entrada[i]))
        else:
            print('O ano {} NAO eh bissexto'.format(entrada[i]))

entrada = list(map(int,input().split()))

mensagem(entrada)