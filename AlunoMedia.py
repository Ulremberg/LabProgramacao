#Aprovado (média >= 7);
#Reprovado (média < 3);
#Prova final ( 3 <= média < 7).


nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = ((nota1 + nota2 + nota3) / 3)

print(media)
if(media >= 7):
    print('aprovado')
elif(media < 3):
    print('reprovado')
elif( media <= 3 or media < 7):
    print('prova final')