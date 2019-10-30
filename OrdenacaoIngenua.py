entrada = int(input())
numeros = sorted([int(input()) for i in range(entrada)])
string = ''
for i in numeros:
    string += "["+str(i)+"]"
print(string)