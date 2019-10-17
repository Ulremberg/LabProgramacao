valorSacar = int(input())

cinquenta = valorSacar // 50
valorSacar = valorSacar % 50

vinte = valorSacar // 20
valorSacar = valorSacar % 20

dez = valorSacar // 10
valorSacar = valorSacar % 10

cinco = valorSacar // 5
valorSacar = valorSacar % 5

um = valorSacar // 1

print("Notas de 50:{}".format(cinquenta))

print("Notas de 20:{}".format(vinte))

print("Notas de 10:{}".format(dez))

print("Notas de 5:{}".format(cinco))

print("Notas de 1:{}".format(um))
