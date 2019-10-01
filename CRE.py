import math
disciplina = {}
disciplinas = []
CRE = 0
somaCH = 0.0
somaDaNota = 0.0

while (True):
    disciplina['semestre'] = int(input())
    if (disciplina['semestre'] <= 0 or disciplina['semestre'] > 10):
        break
    disciplina['cargaHoraria'] = int(input())
    disciplina['nota'] = int(input())
    disciplina['situacao'] = input().strip().upper()
    disciplinas.append(disciplina)
    if disciplina['situacao'] in "ARF":
        if disciplina['cargaHoraria'] in [33, 50, 67, 83]:
            somaDaNota += disciplina['cargaHoraria'] * disciplina['nota']
            somaCH += disciplina['cargaHoraria']
if (somaCH == 0):
    print("entrada invalida")
else:
    CRE = somaDaNota/somaCH
    print("{:.2f}".format(CRE))