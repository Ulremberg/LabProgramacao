#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#As perguntas são:
#  a. "Telefonou para a vítima?"
#  b. "Esteve no local do crime?"
#  c. "Mora perto da vítima?"
#  d. "Devia para a vítima?"
#  e. "Já trabalhou com a vítima?"
#  O programa deve no final emitir uma classificação
#  sobre a participação da pessoa no crime.
#  Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita",
#  entre 3 e 4 como "Cúmplice" e
#  5 como "Assassino".
#  Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima?\n",
    "Esteve no local do crime?\n",
    "Mora perto da vítima?\n",
    "Devia para a vítima?\n",
    "Já trabalhou com a vítima?\n"
]

resposta = 0
for respondido in perguntas:
    if(input(respondido) == "S"):
        resposta += 1
else:
    resposta == resposta


def julgamento(resposta):
    if (resposta == 5):
        return print("Assassino")
    elif (resposta >= 3):
        return print("Cúmplice")
    elif (resposta == 2):
        return print("Suspeito")
    else:
        return print("Inocente")

julgamento(resposta)