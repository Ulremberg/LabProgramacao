entrada = int(input())

valorSacar = entrada

cem = valorSacar // 100
valorSacar = valorSacar % 100

cinquenta = valorSacar // 50
valorSacar = valorSacar % 50

vinte = valorSacar // 20
valorSacar = valorSacar % 20

dez = valorSacar // 10
valorSacar = valorSacar % 10

cinco = valorSacar // 5
valorSacar = valorSacar % 5

dois = valorSacar // 2
valorSacar = valorSacar % 2

um = valorSacar // 1

print("{}".format(entrada))

print("{} nota(s) de R$ 100,00".format(cem))

print("{} nota(s) de R$ 50,00".format(cinquenta))

print("{} nota(s) de R$ 20,00".format(vinte))

print("{} nota(s) de R$ 10,00".format(dez))

print("{} nota(s) de R$ 5,00".format(cinco))

print("{} nota(s) de R$ 2,00".format(dois))

print("{} nota(s) de R$ 1,00".format(um))