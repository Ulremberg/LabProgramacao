def fatorial(number):
    i = 1
    numero_fatorial = 1
    while i <= number:
        n_fat = numero_fatorial * i
        i = i + 1

    print("%d! = %d" % (number, numero_fatorial))


number = int(input('Digite um número: '))
fatorial(number)