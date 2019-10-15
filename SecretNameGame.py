import random
names = {
    'Mary',
    'July',
    'Paul',
    'Julian',
    'Selma',
    'Bob'
}

randomName = random.choice(list(names))
#print(randomName)
flag = False
tentativa = input('Tente adivinhar o nome secreto:\n')

while(flag == False):
    if(tentativa in randomName):
        print('Parabéns vc acertou o nome: {}'.format(tentativa))
        flag = True
    else:
          tentativa = input('Tente novamente:\n')

