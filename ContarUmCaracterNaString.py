palavra = input()
letra = input()
count = 0
for i in palavra:
    if letra == i:
        count = count + 1
print(count)