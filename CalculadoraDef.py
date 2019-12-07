def calculadora(valor1, valor2, operacao):
    if operacao == '1':
        adicao = valor1 + valor2
        print('  ')
        print("O resultado da soma foi: {}".format(adicao))
        print('                                             ')
    elif operacao == '2':

        subtracao = valor1 - valor2
        print(' ')
        print("O resultado da subtração foi: {}".format(subtracao))
        print('                                             ')
    elif operacao == '3':
        multiplicacao = valor1 * valor2
        print('  ')
        print("O resultado da multiplicação foi: {}".format(multiplicacao))
        print('                                             ')
    elif operacao == '4':
        if valor2 == 0:
            print("Entrada inválida")
        else:
            divisao = valor1 / valor2
            print('  ')
            print("O resultado da divisão foi: {}".format(divisao))
            print('                                             ')
    else:
        print('  ')
        print('digite uma opção válida:')
        print('                                             ')


while 0 == 0:
    print('Opções de operação da calculadora:')
    print('1.Adição')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisao')
    print('5.Finalizar a calculadora')
    print('                                             ')

    operacao = input("Digite a operação: ")
    if operacao == '5':
        break
    print('')
    valo1 = int(input("Entre com o primeiro número: "))
    valor2 = int(input("Entre com o segundo número: "))
    calculadora(valo1, valor2, operacao)