livros = int(input())
peso = 0
count = 0
while (livros <= 18):
    count += 1
    peso = peso + livros
    if (peso >= 18):
        print(count - 1)
        break
    else:
        livros = int(input())
