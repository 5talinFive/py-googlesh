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
