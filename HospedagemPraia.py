tipo_apartamento = input().lower()
qtd_dias = int(input())
def Calculo(tipo_apartamento,qtd_dias):
    ind = 125
    suite_tripla = 180
    suite_dupla = 140
    valor = 0

    if tipo_apartamento == "individual":
        valor = ind*qtd_dias
    elif tipo_apartamento == "suíte dupla" or tipo_apartamento == "suítedupla" or tipo_apartamento == "suitedupla" or tipo_apartamento == "suite dupla":
        valor = suite_dupla*qtd_dias
    elif tipo_apartamento == "suíte tripla" or tipo_apartamento == "suítetripla" or tipo_apartamento == "suite tripla" or tipo_apartamento == "suitetripla":
        valor = suite_tripla*qtd_dias
    if qtd_dias > 2:
        valor = valor*0.85
    return valor

print("{:.2f}".format(Calculo(tipo_apartamento, qtd_dias)))