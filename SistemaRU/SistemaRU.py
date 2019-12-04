from flask import Flask, render_template, Response, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/fila', methods=['GET', 'POST'])
def fila():
     if request.method == 'POST':
         data_e_hora_atuais = datetime.now()
         data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
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
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        flag = 0
        while flag == 0:
            arq = open("Vegetarianos", 'a')
            numeroMatricula = input("Digite seu número de matrícula:\n")
            a = 0
            for i in numeroMatricula:
                a += 1
            if (a == 11):
                arq.write(numeroMatricula + "\n")
                flag = flag + 1
                print('Cadastrado')
            else:
                print("Matrícula inválida")

        arq.close()
if __name__ == "__main__":
    app.run()