import pandas as pd
import sodapy import socrata

def consultar_casos_covid(departamento, limite)
    client = socrata("www.datos.gov.co", None)
    resultados = client.get (
        "gt2j-8ykr",
        limit=limite,
        departamento=departamento.upper()
    )

df = pd.DataFrame.from_records(resultados)
return df