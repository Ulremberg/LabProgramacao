# valueingallon = input("Enter value: \n")
#
# GallonToLiter = valueingallon * 3.7854
#
# print("The value in liter is: \n" "{0:4.2f}".format(GallonToLiter))

valorEmGalao = int(input("Entre com o valor: \n"))

GalaoParaLitro = (valorEmGalao * 3.7854)

print("{}" " GALÕES" " -> " "{:.2f}" "LITROS"  .format(valorEmGalao, GalaoParaLitro))

print('{} GALÕES -> {:.2f} LITROS' .format(valorEmGalao, GalaoParaLitro))

#print(%valorEmGalao, " GALÕES", %GalaoParaLitro,"%.2f LITROS")

#25 GALÕES -> 94.64 LITROS

const = 3.7854

galão = int(input())
resposta = (galão * const)

if(galão == 0 ):
    print(galão, "GALÕES ->", "0.00", "LITROS")

a = round(resposta, 2)
if(galão == 1):
    print(galão, "GALÃO ->" , a ,  "LITROS")
if(galão > 1):
    print(galão, "GALÕES ->" , a , "LITROS")