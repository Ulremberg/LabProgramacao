qtdCoisas = int(input())
coisas = []
for i in range(qtdCoisas):
       coisas.append(input())
qtdFinal = int(input())
for i in range(qtdFinal):
       i = input()
       if (i not in coisas):
              continue
       else:
              coisas.remove(i)
if (len(coisas) == 0):
       print("Smelly Cat, Smelly Cat, what are they feeding you?")
else:
       print("Ainda falta(m) {} objetivo(s)!".format(len(coisas)))
       for i in coisas:
              print(i)