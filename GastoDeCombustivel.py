print('Digite o tempo gasto (em horas) e a velocidade media (em km/h):')
entrada1 = float(input())
entrada2 = float(input())

distancia = entrada1 * entrada2

print('Quantidade de litros gastos na viagem: {:.6f}'.format(distancia/12.0))