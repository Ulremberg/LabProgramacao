# Escreva um programa que receba o raio (R) de uma esfera e forneça:
#
# a) A área da superfície esférica,sabendo que Área Superfície=4πR2
#
# b) O volume de uma esfera, sabendo que Volume = (4πR3)/3
#
# Observação: Considere π como tendo o valor 3.1416.

radius = float(input())

surfaceArea = ((4 * 3.1416) * (radius ** 2))

volume = (((4 * 3.1416) * (radius ** 3 )) / 3)

print('{:.2f}\n{:.2f}'.format(surfaceArea, volume))