#O usuario deve digitar os valores (inteiros) da base menor, da base maior e da altura.
# (((basemaior + basemenor) * altura) / 2)

baseMenor = int(input('Digite a base menor:\n'))
baseMaior = int(input('Digite a base maior:\n'))
altura = int(input('Digite a altura:\n'))

area = (((baseMaior + baseMenor) * altura) / 2)

print('Area do trapezio: {}'.format(area))