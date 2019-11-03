vetor=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
entrada=input()
if len(entrada) > 6:
  vetor[6] = entrada[6]
  vetor = ''.join(vetor)
  if vetor[6] == "b":
    print("Bulbassauro")
  elif vetor[6] == "c":
    print("Charmander")
  elif vetor[6] == "s":
    print("Squirtle")
  else:
    print("Codigo Invalido")
else:
  print("Codigo Invalido")