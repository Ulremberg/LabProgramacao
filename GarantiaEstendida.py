preco = float(input())
anos_garantia = int(input())
taxa = 0
if anos_garantia == 1:
    taxa = preco * 0.03
elif anos_garantia == 2:
    taxa = preco * 0.05
total = preco + taxa


print('{:.2f}'.format(total))