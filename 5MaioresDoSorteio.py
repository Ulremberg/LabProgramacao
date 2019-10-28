entrada = input()
entradaInt = int(entrada.split()[0])
D = entrada.split()[1]
vetor =[]
for i in range(entradaInt):
    num = input()
    if (num[len(num)-1] == D):
        vetor.append(int(num))
    else:
        vetor.append(-1)
vetor.sort(reverse=True)
vetor = vetor[0:5]
vetor.sort()
for i in vetor:
    print(i)