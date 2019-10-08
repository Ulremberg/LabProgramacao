def calculator(x,y,z):
    if(z == '*'):
        multiplicacao = x * y
        print(multiplicacao)
    elif(z == '-'):
        subtracao = x - y
        print(subtracao)
    elif(z == '/'):
        if(y == 0):
            print('Entrada inválida')
        else:
            div = x / y
            print(div)
    elif(z == '+'):
        soma = x + y
        print(soma)
    else:
        print('Digite uma operação válida')

calculator(10,5,'/')
