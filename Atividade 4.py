# coding: utf-8
base=int(input('Informe a base:'))
valorBase = base
expoente=int(input('\nInforme o expoente:'))
if (expoente==1) or (expoente==0):
  if (expoente==1):
     print('\nResultado: %s' % (base))
  else:
    print('\nResultado: 1')
else:
  for i in (range(expoente-1)):
    base*=valorBase
  print('\nResultado: %s' % (base))