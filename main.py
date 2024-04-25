from google.oauth2 import service_account
from googleapiclient.discovery import build

def agregar_fila_a_spreadsheet(service, spreadsheet_id, range_name, new_row):
    """
    Agrega una nueva fila a la hoja de cálculo especificada.

    Args:
        service: Objeto del servicio de Google Sheets.
        spreadsheet_id (str): ID de la hoja de cálculo.
        range_name (str): Nombre del rango en la hoja de cálculo.
        new_row (list): Lista que representa la nueva fila a agregar.
    """
    service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption='RAW',
        body={'values': [new_row]}
    ).execute()

def ingresar_datos_por_teclado():
    """
    Solicita al usuario que ingrese los datos para una nueva fila.

    Returns:
        list: Lista que representa los datos ingresados por el usuario.
    """
    new_row = []
    print("Ingrese los datos para la nueva fila:")
    new_row.append(input("Nombre: "))
    new_row.append(input("Curso: "))
    new_row.append(input("Centro de atención: "))
    new_row.append(input("Nota U1: "))
    new_row.append(input("Nota U2: "))
    new_row.append(input("Nota U3: "))
    new_row.append(input("Nota U4: "))
    return new_row

def eliminar_datos_fila_por_teclado(service, spreadsheet_id, sheet_name):
    """
    Elimina los datos de una fila en la hoja de cálculo especificada,
    solicitando al usuario el número de fila por teclado.

    Args:
        service: Objeto del servicio de Google Sheets.
        spreadsheet_id (str): ID de la hoja de cálculo.
        sheet_name (str): Nombre de la hoja de cálculo.
    """
    # Solicitar al usuario el número de fila
    row_index = int(input("Ingrese el número de fila que desea limpiar: "))

    # Construir el rango del número de fila
    range_name = f"{sheet_name}!{row_index}:{row_index}"

    # Eliminar los datos de la fila especificada
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()

def menu_principal():
    while True:
        print("\n[*** MENÚ] *** ")
        print("[L] Listar datos")
        print("[C] Crear nuevos datos")
        print("[D] Eliminar datos")
        print("[S] Salir")
        
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == "L":
            listar_datos(service, SPREADSHEET_ID, range_name)
        elif opcion == "C":
            crear_nuevos_datos(service, SPREADSHEET_ID, range_name)
        elif opcion == "D":
            eliminar_datos(service, SPREADSHEET_ID, 'datafinal')
        elif opcion == "S":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def listar_datos(service, spreadsheet_id, range_name):
    """
    Lista los datos en la hoja de cálculo especificada.

    Args:
        service: Objeto del servicio de Google Sheets.
        spreadsheet_id (str): ID de la hoja de cálculo.
        range_name (str): Nombre del rango en la hoja de cálculo.
    """
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=range_name
    ).execute()
    values = result.get('values', [])
    
    if values:
        header = values[0]
        data = values[1:]
        
        print("Encabezado:")
        print(header)
        
        print("\nDatos:")
        for row in data:
            print(row)
    else:
        print("No se encontraron datos en el rango especificado.")

def crear_nuevos_datos(service, spreadsheet_id, range_name):
    """
    Permite al usuario ingresar nuevos datos y los agrega a la hoja de cálculo especificada.

    Args:
        service: Objeto del servicio de Google Sheets.
        spreadsheet_id (str): ID de la hoja de cálculo.
        range_name (str): Nombre del rango en la hoja de cálculo.
    """
    nueva_fila = ingresar_datos_por_teclado()
    datos_actualizados = agregar_fila_a_spreadsheet(service, spreadsheet_id, range_name, nueva_fila)
    print("Se han agregado los nuevos datos correctamente.")

def eliminar_datos(service, spreadsheet_id, sheet_name):
    """
    Permite al usuario ingresar el número de fila que desea eliminar y elimina los datos de esa fila
    en la hoja de cálculo especificada.

    Args:
        service: Objeto del servicio de Google Sheets.
        spreadsheet_id (str): ID de la hoja de cálculo.
        sheet_name (str): Nombre de la hoja de cálculo.
    """
    eliminar_datos_fila_por_teclado(service, spreadsheet_id, sheet_name)
    print("Se han eliminado los datos correctamente.")


# Inicio del programa
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
menu_principal()
