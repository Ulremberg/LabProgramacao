def fatorial(number):
    f = 1
    for i in range(number, 0, -1):
        print(i, end='')
        if (i > 1):
            print(' x ', end='')
        else:
            print(' = ', end='')

        f *= i

    print('{}'.format(f))

fatorial(5)

