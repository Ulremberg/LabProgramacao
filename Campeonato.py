# A entrada é descrita em uma única linha, que contém seis inteiros, separados por um
# espaço em branco. Cv ,Ce, Cs, Fv, Fe, Fs, que são, respectivamente, o número de vitórias
# do Cormengo, o número de empates do Cormengo, o saldo de gols do Cormengo, o
# número de vitórias do Flaminthians, o número de empates do Flaminthians e o saldo de
# gols do Flaminthians.
#
# Considere:
#
# 0 <= Cv, Ce, Fv, Fe <= 100
# -1000 <= Cs, Fs <= 1000

a = input().split()

CormengoVitoria = int(a[0])
CormengoEmpate = int(a[1])
CormengoSaldo = int(a[2])
FlamithiansVitoria = int(a[3])
FlamithiansEmpate = int(a[4])
FlamithiansSaldo = int(a[5])

Cv = CormengoVitoria * 3
Ce = CormengoEmpate * 1

Fv = FlamithiansVitoria * 3
Fe = FlamithiansEmpate * 1

Flamithians = Fv + Fe
Cormengo = Cv + Ce

if(Cormengo > Flamithians):
    print("C")
elif(Cormengo < Flamithians):
    print("F")
elif(Flamithians == Cormengo and FlamithiansSaldo > CormengoSaldo):
    print("F")
elif(Cormengo == Flamithians and CormengoSaldo > FlamithiansSaldo):
    print("C")
elif(Cormengo == Flamithians and CormengoSaldo == FlamithiansSaldo):
    print("=")