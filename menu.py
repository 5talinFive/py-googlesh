from google.oauth2 import service_account
from googleapiclient.discovery import build
from leer import listar_datos
from crear import agregar_fila_a_spreadsheet, ingresar_datos_por_teclado
from eliminar import eliminar_datos_fila_por_teclado

def menu_principal(service, spreadsheet_id, range_name):
    while True:
        print("\n[MENÚ]")
        print("[L] Listar datos")
        print("[C] Crear nuevos datos")
        print("[D] Eliminar datos")
        print("[S] Salir")
        
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == "L":
            listar_datos(service, spreadsheet_id, range_name)
        elif opcion == "C":
            nueva_fila = ingresar_datos_por_teclado()
            agregar_fila_a_spreadsheet(service, spreadsheet_id, range_name, nueva_fila)
            print("Se han agregado los nuevos datos correctamente.")
        elif opcion == "D":
            eliminar_datos_fila_por_teclado(service, spreadsheet_id, 'datafinal')
            print("Se han eliminado los datos correctamente.")
        elif opcion == "S":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Credenciales de servicio
SCOPE = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/spreadsheets']
KEY = 'key.json'
SPREADSHEET_ID = '16A-aMMGLvwX1AYrlHNdxILNmFGyZoMH9yxVQ8mApwVI'

# Credenciales de servicio
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPE)

# Construye el servicio de Google Sheets
service = build('sheets', 'v4', credentials=creds)

# Define el rango que cubre todas las filas y columnas del CSV (por ejemplo, A1:ZZ)
range_name = 'datafinal'

# Ejecutar el menú principal
menu_principal(service, SPREADSHEET_ID, range_name)
