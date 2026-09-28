import pandas as pd
from sodapy import Socrata

def consultar_casos_covid(departamento, limite):
    # Conexión a la API pública de Datos Abiertos
    client = Socrata("www.datos.gov.co", None)
    
    # 1. Asegurar mayúsculas y quitar espacios extra
    depto_formateado = departamento.strip().upper()
    
    # 2. Filtrar en la columna 'departamento_nom' usando comillas simples
    resultados = client.get(
        "gt2j-8ykr",
        limit=limite,
        where=f"departamento_nom='{depto_formateado}'"
    )
    
    # 3. Convertir resultados a DataFrame
    df = pd.DataFrame.from_records(resultados)
    return df