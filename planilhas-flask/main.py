from flask import Flask, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials


app = Flask(__name__)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('static/credentials.json', scope)

client = gspread.authorize(credentials)

@app.route('/')
def index():
    sheet = client.open_by_key('1XvWJcRLj2WAeXO3ULQ_GxGm9---3SZkjMbGcXMJtt70')
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_values()
    tamanho = len(data)

    matricula = [row[0] for row in data[3:]]  
    aluno = [row[1] for row in data [3:]]  
    faltas = [row[2] for row in data[3:]]
    p1 = [int(row[3]) for row in data[3:]]
    p2 = [int(row[4]) for row in data[3:]]
    p3 = [int(row[5]) for row in data[3:]]
   

    return render_template('index.html', tamanho = tamanho, matricula = matricula, aluno = aluno, faltas = faltas, p1 = p1, p2 = p2, p3 = p3)  # Passe as colunas como variáveis separadas


if __name__ == '__main__':
    app.run(debug=True)
