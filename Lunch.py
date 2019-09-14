escolhaComida = [["lasanha", "estrogonofe"], [8, 11]]
bebida = [["refrigerante", "suco"], [3, 2.5]]

comida = input()
beb = input()
for i in range(2):
    if comida.lower() == escolhaComida[0][i]:
        for j in range(2):
            if beb.lower() == bebida[0][j]:
                total = escolhaComida[1][i] + bebida[1][j]

#print("%.2f" % total)
print('{:.2f}'.format(total))
