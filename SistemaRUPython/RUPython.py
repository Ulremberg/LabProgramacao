from datetime import datetime
data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
print("**********************************","\nBem Vindo ao Sistema RU.", "\nDigite fila - Para saber a quantidade da fila.",
      "\nDigite Vege - Para se cadastra no cardapio vegetariano.",
      "\nDigite Lista - Para ver a lista dos vegetarianos.", "\nDigite o dia da semana pra saber o cardápio.",
      "\nDigite Sair - Para finalizar o programa")
Entrada = input("O que você quer fazer: ").upper()

while Entrada != "SAIR":
    if(Entrada == "FILA"):
        if (data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto < "10:30"):
            print(data_e_hora_em_texto)
            print("O RU está fechado, volte mais tarde.")
        elif (data_e_hora_em_texto >= "10:30" and data_e_hora_em_texto < "11:00"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "11:00" and data_e_hora_em_texto < "11:30"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "12:00" and data_e_hora_em_texto < "12:30"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "12:30" and data_e_hora_em_texto < "13:00"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "13:00" and data_e_hora_em_texto < "13:30"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "14:00" and data_e_hora_em_texto < "16:30"):
            print(data_e_hora_em_texto)
            print("O RU está fechado, volte mais tarde.")
        elif (data_e_hora_em_texto >= "16:30" and data_e_hora_em_texto < "17:00"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "17:50" and data_e_hora_em_texto < "18:00"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "18:30" and data_e_hora_em_texto < "19:00"):
            print(data_e_hora_em_texto)
            print("X pessoas")
        elif (data_e_hora_em_texto >= "19:00" and data_e_hora_em_texto <= "23:59"):
            print(data_e_hora_em_texto)
            print("O RU está fechado, volte mais tarde.")


    elif (Entrada == "VEGE"):
        flag = 0
        while flag == 0:
            arq = open("Vegetarianos", 'a')
            ve = input("Digite seu número de matrícula:\n")
            a = 0
            for i in ve:
                a += 1
            if (a == 11):
                arq.write(ve + "\n")
                flag = flag + 1
                print('Cadastrado')
            else:
                print("Matricula inválida")

        arq.close()

    elif(Entrada == "LISTA"):
        arq = open("Vegetarianos", 'r')
        while (arq != ''):
            dado = arq.readline()
            print(dado)
        arq.close()

    elif(Entrada == "SEGUNDA"):
        if(data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto <= "14:00"):
            print(" PRINCIPAL PRATO 1 - FRANGO ASSADO À MODA DO CHEFE","\n PRINCIPAL 2 - ISCA DE CARNE À BRASILEIRA (COM CALABRESA)","\n NAGRELHA - FRANGO COM BATATA DOCE",
                  "\n GRELHA RÁPIDA - VIRADO PAULISTA","\n VEGETARIANO - BOLONHESA DE LENTILHA COM TALHARIM","\n GUARNIÇÃO - QUEBEBE / ARROZ / CHEIRO VERDE / FEIJÃO PRETO",
                  "\n SALADA CRUA - ACELGA COM AGRIÃO E LARANJA","\n SALADA COZIDA - BETERRABA COM CEBOLINHO","\n SOBREMESA - MELANCIA","\n SUCO - MANGA / LIMÃO")
        elif(data_e_hora_em_texto > "14:00" and data_e_hora_em_texto <= "23:59"):
            print(" PRINCIPAL PRATO 1 - PEITO DE FRANGO COM PALHA","\n PRINCIPAL 2 DO PRATO - CARNE MOÍDA COM AZEITONAS","\n NAGRELHA - ISCAS DE CARNE ACEBOLADA (ACOMP. MACAXEIRAO)",
                  "\n VEGETARIANO - NUGGTES DE MILHO","\n GRELHA RÁPIDA - ...","\n GUARNIÇÃO - CUSCUZ","\n SOPA - SOPA DE CREME DE MACAXEIRA","\n SALADA CRUA - TOMATE / CHICÓRIA / HORTELÃ",
                  "\n SOBREMESA - MELANCIA","\n SUCO - MANGA / LIMÃO")
    elif (Entrada == "TERÇA"):
        if (data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto <= "14:00"):
            print(" PRINCIPAL PRATO 1 - COPA LOMBO COM FRUTAS","\n PRINCIPAL PRATO 2 - FRANGO COM CREME DE MILHO","\n NAGRELHA - CARNE ASSADA COM LEGUMES E MACARRÃO INTEGRAL",
                  "\n GRELHA RÁPIDA - ESCONDIDINHO","\n VEGETARIANO - ESTROGONOFE DE GRÃO DE BICO","\n GUARNIÇÃO - REPOLHO GRATINADO / ARROZ COM MILHO / FEIJÃO CARIOCA",
                  "\n SALADA CRUA - ALFACE COM RÚCULA E ABACAXI","\n SALADA COZIDA - CENOURA COM VAGEM","\n SOBREMESA - CHOCOLATE","\n SUCO - GOIABA / UMBU")
        elif (data_e_hora_em_texto > "14:00" and data_e_hora_em_texto <= "23:59"):
            print(" PRINCIPAL PRATO 1 - BIFE AO MOLHO FERRUGEM","\n PRATO PRINCIPAL 2 - PEIXE À DELÍCIA","\n NAGRELHA - FRANGO AO FORNO COM ERVAS (ACOMP. BATATA DOCE",
                  "\n VEGETARIANO - QUICHE DE ESPINAFRE","\n GRELHA RÁPIDA - PARMEGIANA DE FRANGO","\n GUARNIÇÃO - ARROZ COLORIDO","\n SOPA - SOPA CRIOULA (SEM MACARRÃO)",
                  "\n SALADA CRUA - ALFACE COM PEPINO E GERGELIM","\n SOBREMESA - CHOCOLATE","\n SUCO - GOIABA / UMBU")
    elif (Entrada == "QUARTA"):
        if (data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto <= "14:00"):
            print(" PRINCIPAL PRATO 1 - PEITO DE FRANGO COM ERVILHAS","\n PRINCIPAL PRATO 2 - CARNE ASSADA AO MOLHO FERRUGEM","\n NAGRELHA - PEIXE COM ABOBRINHA E TOMA EM CUBOS",
                  "\n GRELHA RÁPIDA - BAIÃO DE DOIS","\n VEGETARIANO - TORTA DE LEGUMES VEGETARIANO","\n GUARNIÇÃO - ESPAGUETE COM MOLHO PESTO / ARROZ COLORIDO / FEIJÃO PRETO",
                  "\n SALADA CRUA - PEPINO COM TOMATE E MANJERICÃO","\n SALADA COZIDA - BATATAS COM COUVE E CEBOLA ROXA","\n SOBREMESA - MAMÃO","\n SUCO - TANGERINA / CAJU")
        elif (data_e_hora_em_texto > "14:00" and data_e_hora_em_texto <= "23:59"):
            print(" PRINCIPAL PRATO 1 - CARNE TAILANDESA (COM MOLHO DE CURRY, SHOYU E PIMENTÕES)","\n PRINCIPAL PRATO 2 - FRANGO ASSADO C / PARMESSÃO","\n NAGRELHA - BIFE COM PIMENTÕES",
                  "\n VEGETARIANO - BOLINHO DE MACAXEIRA COM MOLHO","\n GRELHA RÁPIDA - CREPE","\n GUARNIÇÃO - BATATA DOCE","\n SOPA - SOPA DE LEGUMES","\n SALADA CRUA - BETERRABA, ACELGA E CENOURA",
                  "\n SOBREMESA - MAMÃO","\n SUCO - TANGERINA / CAJU")
    elif (Entrada == "QUINTA"):
        if (data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto <= "14:00"):
            print(" PRINCIPAL PRATO 1 - BIFE AO MOLHO MADEIRA","\n PRATO PRINCIPAL 2 - PEIXE À ZÉ DO PIPO","\n NAGRELHA - FRANGO GRELHADO COM PIMENTÕES","\n GRELHA RÁPIDA - QUICHE DE FRANGO",
                  "\n VEGETARIANO - ACARAJÉ VEGETARIANO","\n GUARNIÇÃO - ABÓBORA REFOGADA / ARROZ COM ERVILHAS / FEIJÃO CARIOCA","\n SALADA CRUA - CENOURA / ACELGA / TOMATE / PASSAS",
                  "\n SALADA COZIDA - ABOBRINHA COM PIMENTÕES COLORIDOS","\n SOBREMESA - DOCE GOIABADA AÇUCARADO","\n SUCO - UVA / ABACAXI COM HORTELÃ")
        elif (data_e_hora_em_texto > "14:00" and data_e_hora_em_texto <= "23:59"):
            print(" PRINCIPAL PRATO 1 - FRANGO GRELHADO À PRIMAVERA","\n PRATO PRINCIPAL 2 - CHURRASQUEIRA ALMÔNDEGA AO MOLHO","\n NAGRELHA - PEITO DE FRANGO COM ABÓBORA","\n VEGETARIANO - VEGETARIANO NHOQUE",
                  "\n GRELHA RÁPIDA - LASANHA DE FRANGO","\n GUARNIÇÃO - ESPAGUETE","\n SOPA - CALDO VERDE","\n SALADA CRUA - MISTURA DE FOLHAS COM REPOLHO ROXO","\n SOBREMESA - DOCE GOIABADA AÇUCARADO",
                  "\n SUCO - UVA / ABACAXI COM HORTELÃ")
    elif (Entrada == "SEXTA"):
        if (data_e_hora_em_texto >= "00:00" and data_e_hora_em_texto <= "14:00"):
            print(" PRATO PRINCIPAL 1 - DOBRADINHA","\n PRATO PRINCIPAL 2 - PEITO DE FRANGO COM PALHA","\n NAGRELHA - BIFE GRELHADO COM CEBOLA (ACOMP. MACARRÃO INTEGRAL)",
                  "\n GRELHA RÁPIDA - CROQUETA DE FRANGO AO MOLHO ROSÉ","\n VEGETARIANO - PANQUECA DE ESPINAFRE","\n GUARNIÇÃO - FAROFA DOURADA / ARROZ BRANCO / FEIJÃO CARIOCA",
                  "\n SALADA CRUA - VINAGRETE","\n SALADA COZIDA - CHUCHU COM CENOURA E AZEITONAS","\n SOBREMESA - BANANA","\n SUCO - CAJÁ / ACEROLA")
        elif (data_e_hora_em_texto > "14:00" and data_e_hora_em_texto <= "23:59"):
            print(" PRATO PRINCIPAL 1 - CARNE DE SOL ACEBOLADA","\n PRATO PRINCIPAL 2 - FRANGO AO MOLHO DE TOMATE COM MANJERICÃO","\n NAGRELHA - PEIXE COM LIMÃO","\n VEGETARIANO - BERINJELA À PARMEGIANA COM ESPAGUETE",
                  "\n GRELHA RÁPIDA - ...","\n GUARNIÇÃO - MACAXEIRA","\n SOPA - CREME DE ABÓBORA","\n SALADA CRUA - TOMATE COM CEBOLA ROXA E ACELGA","\n SOBREMESA - BANANA",
                  "\n SUCO - CAJU / ACEROLA")
    elif(Entrada == "SAIR"):
        break
    print("**********************************", "\nBem Vindo ao Sistema RU.",
          "\nDigite fila - Para saber a quantidade da fila.",
          "\nDigite Vege - Para se cadastra no cardapio vegetariano.",
          "\nDigite Lista - Para ver a lista dos vegetarianos.", "\nDigite o dia da semana pra saber o cardápio.",
          "\nDigite Sair - Para finalizar o programa")
    Entrada = input("O que você quer fazer: ").upper()