dias = int(input())
kilometros_rodados = int(input())

valorDiaFinal = dias * 30.0
valorKmFinal = kilometros_rodados * 0.01

desconto = (valorDiaFinal + valorKmFinal) * 0.10
total = (valorDiaFinal + valorKmFinal) - desconto

print('{:.2f}'.format(total))
