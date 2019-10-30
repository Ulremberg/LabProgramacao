def CalculoNota(nota1, nota2, nota3, nota4):
    media = (nota1 + (nota2 * 2) + (nota3 * 3) + (nota4 * 4)) / 10
    if media >= 9:
        print("aprovado com louvor")
    elif media >= 7:
        print("aprovado")
    elif media < 3:
        print("reprovado")
    else:
        print("prova final")


entrada = input().split()
nota1 = float(entrada[0])
nota2 = float(entrada[1])
nota3 = float(entrada[2])
nota4 = float(entrada[3])
CalculoNota(nota1, nota2, nota3, nota4)
