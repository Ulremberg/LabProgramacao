lista=[]
contador=0
contador2=0
notas=int(input())
if (notas == 0):
  print("Numero de notas invalido.")
else:
  while (contador < notas):
    lista.append(float(input()))
    contador +=1
  media = (sum(lista) / notas)
  for i in range(notas):
    #print("Nota ", contador2 + 1, ": ", lista[contador2], sep="")
    print('Nota {}: {}'.format(contador2+1, lista[contador2], sep=""))
    contador2+=1
  print("Media: {:.2f}".format(media))