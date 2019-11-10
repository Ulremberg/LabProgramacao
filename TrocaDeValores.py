def troca(a, b):
    print('a: {} b: {}'.format(a, b))
    a, b = b, a
    print('a: {} b: {}'.format(a, b))


z = input().split()

a = z[0]
b = z[1]
troca(a, b)