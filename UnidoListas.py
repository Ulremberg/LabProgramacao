elementosLista1 = int(input())
lista1 = [0] * (elementosLista1)

if (elementosLista1 <= 0):
    print("Erro - A lista deve ter pelo menos 1 elemento.")

else:
    for i in range(elementosLista1):
        valoresLista1 = int(input())
        lista1[i] = valoresLista1

    elementosLista2 = int(input())
    lista2 = [0] * (elementosLista2)

    if (elementosLista2 <= 0):
        print("Erro - A lista deve ter pelo menos 1 elemento.")
    else:
        for x in range(elementosLista2):
            valoresLista2 = int(input())
            lista2[x] = valoresLista2

        listaImprimir = lista1 + lista2

        for i in range(len(listaImprimir)):
            print(listaImprimir[i], end=" ")