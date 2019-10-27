entrada = int(input())
count = 0
soma = 0
while (entrada != 0):
    count += 1
    soma = soma + entrada
    entrada = int(input())
media = soma/count
if(media<110):
    print("Glicose Normal")
elif(media >= 200):
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")