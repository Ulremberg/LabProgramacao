from flask import Flask, render_template, Response, request, redirect, url_for
from datetime import datetime
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/fila', methods=['GET', 'POST'])
def fila():
     if request.method == 'POST':
         data_e_hora_atuais = datetime.now()
         data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
         if (data_e_hora_em_texto > "10:30" and data_e_hora_em_texto < "11:00"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "11:00" and data_e_hora_em_texto < "11:30"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "12:00" and data_e_hora_em_texto < "12:30"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "12:30" and data_e_hora_em_texto < "13:00"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "13:00" and data_e_hora_em_texto < "13:30"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "14:00" and data_e_hora_em_texto < "16:30"):
             print("O RU está fechado, Volte mais tarde.")
         elif (data_e_hora_em_texto >= "16:30" and data_e_hora_em_texto < "17:00"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "17:50" and data_e_hora_em_texto < "18:00"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "18:30" and data_e_hora_em_texto < "19:00"):
             print("X pessoas")
         elif (data_e_hora_em_texto >= "19:00" and data_e_hora_em_texto < "10:29"):
             print("O RU está fechado, Volte mais tarde.")

if __name__ == "__main__":
    app.run()