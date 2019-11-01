numero = int(input())
count = 0
while (numero >= 0):
    for i in range(1, numero + 1):
        if (numero % i == 0):
            count += 1
    if (count == 2):
        print('1')
    else:
        print('0')
    count = 0
    numero = int(input())
    if (numero < 0):
        break
