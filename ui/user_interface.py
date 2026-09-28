def pedir_datos(): 
    departamentos = input("ingrese el nombre del departamento: ").strip()
    limites = int(input("ingrese el límite de resultados: "))
    return departamentos, limites

def mostrar_tabla(df):
    if df.empty:
        print("No se encontraron resultados para el departamento especificado.")
    else:
        columnas = ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio', 'estado', 'pais_viajo_1_nom']
        df_filtrado = df[columnas]
        df_renombrado = df_filtrado.rename(columns={'ciudad_municipio_nom': 'Ciudad de ubicacion', 'departamento_nom': 'Departamento', 'edad': 'Edad', 'fuente_tipo_contagio': 'Tipo', 'estado': 'Estado', 'pais_viajo_1_nom': 'País de procedencia'})
        print(df_renombrado.to_string(index=False))