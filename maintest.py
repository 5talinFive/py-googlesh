from google.oauth2 import service_account
from googleapiclient.discovery import build


SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'

# ID del documento csv (url desde d/ID/edit)
SPREADSHEET_ID = '16A-aMMGLvwX1AYrlHNdxILNmFGyZoMH9yxVQ8mApwVI'

# Credenciales de servicio
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPE)

# Construye el servicio de Google Sheets
service = build('sheets', 'v4', credentials=creds)

# Define el rango que cubre todas las filas y columnas del CSV (por ejemplo, A1:ZZ)
range_name = 'datafinal'

# Llama a la API de Google Sheets para obtener los datos del rango especificado
result = service.spreadsheets().values().get(
    spreadsheetId=SPREADSHEET_ID,
    range=range_name
).execute()

# Extrae los valores del resultado
values = result.get('values', [])

# Si hay valores, el primer elemento es el encabezado y el resto son filas de datos
if values:
    header = values[0]
    data = values[1:]
    
    # Imprime el encabezado
    print("Encabezado:")
    print(header)
    
    # Imprime las filas de datos
    print("\nDatos:")
    for row in data:
        print(row)
else:
    print("No se encontraron datos en el rango especificado.")



# Crear un nuevo dato
# new_row = ['Stalin Sarango', 'Tlgo', 'el coca', '7', '7', '7', '7']
# service.spreadsheets().values().append(
#     spreadsheetId=SPREADSHEET_ID,
#     range=range_name,
#     valueInputOption='RAW',
#     body={'values': [new_row]}
# ).execute()


# Actualizar un dato en una celda específica
update_value = 'Elver'
service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='datafinal!A1336',  # Celda a actualizar
    valueInputOption='RAW',
    body={'values': [[update_value]]}
).execute()


# Eliminar el contenido de una celda específica
# service.spreadsheets().values().clear(
#     spreadsheetId=SPREADSHEET_ID,
#     range='datafinal!A1336'  # Celda a borrar
# ).execute()




if __name__ == '__main__':
    print("todo ok")






