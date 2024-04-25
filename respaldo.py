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

# Ejemplo de uso:
# Suponiendo que tienes ya definido 'service', 'SPREADSHEET_ID' y 'sheet_name'
eliminar_datos_fila_por_teclado(service, SPREADSHEET_ID, 'datafinal')