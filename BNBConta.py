# receba um valor do usuário (correspondente ao saldo da conta), outro valor do usuário
# (correspondente ao valor da transação) e uma operação (débito ou crédito), e depois da
# transação apresente o novo saldo da conta

print('Bem vindo ao Banco do Nordeste defina qual a operação deseja realizar')
saldoConta = float(input('Informe saldo da conta:\n'))
print('Defina qual a operação deseja realizar')
operacao = int(input('Digite 1 se deseja realizar depósito, 2 para saque e 3 para transferência\n'))
if(operacao == 1):
    valorTransacao = float(input('Digite o valor que deseja depositar'))
    saldoConta = saldoConta + valorTransacao
    print('O novo saldo da conta é: {}'.format(saldoConta))
elif(operacao == 2):
    valorTransacao = float(input('Digite o valor do saque'))
    flag = False
    while(flag == False):
        if(saldoConta >= valorTransacao):
            saldoConta = saldoConta - valorTransacao
            print('Operação realizada com sucesso')
            print('O novo saldo da conta é: {}'.format(saldoConta))
            True
            break
        else:
            print('Operação inválida')
            valorTransacao = float(input('Digite o valor do saque'))
elif(operacao == 3):
    valorTransacao = float(input('Digite o valor da transferência'))
    flag = False
    while (flag == False):
        if (saldoConta >= valorTransacao):
            saldoConta = saldoConta - valorTransacao
            print('Operação realizada com sucesso')
            print('O novo saldo da conta é: {}'.format(saldoConta))
            True
            break
        else:
            print('Operação inválida')
            valorTransacao = float(input('Digite o valor do saque'))
else:
    print('Valor de operação inválida')
