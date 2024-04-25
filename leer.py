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