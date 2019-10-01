matriz = []
n = 2
for i in range(n):
   tmp = []
   for j in range(n):
       elemento = input("Digite o elemento da posicao {0}-{1}".format(i,j))
       tmp.append(elemento)

   matriz.append(tmp[:])
print(matriz)