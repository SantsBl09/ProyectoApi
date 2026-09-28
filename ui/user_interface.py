def pedir_datos(): 
    departamentos = input("ingrese el nombre del departamento: ").strip()
    limites = int(input("ingrese el límite de resultados: "))
    return departamentos, limites

def mostrar_tabla(df):
    if df.empty:
        print("\nNo se encontraron resultados para el departamento especificado.")
        return

    # 1. Lista de las 6 columnas requeridas por el profesor
    columnas_requeridas = [
        'ciudad_municipio_nom', 
        'departamento_nom', 
        'edad', 
        'fuente_tipo_contagio', 
        'estado', 
        'pais_viajo_1_nom'
    ]
    
    # 2. Garantizar que existan todas las columnas en el DataFrame (si falta alguna, se llena con 'N/A')
    for col in columnas_requeridas:
        if col not in df.columns:
            df[col] = 'N/A'
            
    # 3. Filtrar exactamente las 6 columnas
    df_filtrado = df[columnas_requeridas]
    
    # 4. Renombrar los encabezados según la guía del taller
    df_renombrado = df_filtrado.rename(columns={
        'ciudad_municipio_nom': 'Ciudad de ubicación',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'fuente_tipo_contagio': 'Tipo',
        'estado': 'Estado',
        'pais_viajo_1_nom': 'País de procedencia'
    })
    
    # 5. Imprimir la tabla formateada
    print("\n" + "="*85)
    print("RESULTADOS DE LA CONSULTA COVID-19")
    print("="*85)
    print(df_renombrado.to_string(index=False))