TVideo = float(input())
TAudio = float(input())
TDados = float(input())
Capacidade = float(input())

if(Capacidade < 0 ):
    Capacidade = input()
else:
    Capacidade

QDmax = ((TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade)

print("{}" .format(round(QDmax, 2)))