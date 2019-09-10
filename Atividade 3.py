# coding: utf-8
num = 0
n = int(input("Digite um número: "))
while num <= 9:
 m = n*(num+1)
 num += 1
 print("{} X {} = {}".format(n, num, m))
