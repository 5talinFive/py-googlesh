from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
# csv_url = 'https://drive.google.com/drive/u/0/my-drive'
KEY = 'key.json'

#ID del documento csv (url desde d/ID/edit)
SPREADSHEETS_ID = '16A-aMMGLvwX1AYrlHNdxILNmFGyZoMH9yxVQ8mApwVI'

cred = None
cred = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPE)

service = build('sheets', 'v4', credentials=cred)
sheet = service.spreadsheets()

#llamado a la api
result = sheet.values().get(spreadsheetId=SPREADSHEETS_ID, range='datafinal!A1:A1335',).execute()

#Extraemos values
values = result.get('values', [])
print(values)







