import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define o escopo da API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# Carrega as credenciais do arquivo JSON
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Autoriza as credenciais
client = gspread.authorize(credentials)

def index():
    sheet = client.open_by_key('1XvWJcRLj2WAeXO3ULQ_GxGm9---3SZkjMbGcXMJtt70')

    # Seleciona a primeira aba
    worksheet = sheet.get_worksheet(0)

    data = worksheet.get_values()

    for i in data:
        q = i;
        print(q)

index();