import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

# Reemplazar formato de fecha a DD-MM-YYYY HH:MM:SS
print("Reemplazando formato de fecha")
vh['posting_date'] = vh['posting_date'].apply(lambda x: pd.to_datetime(x).strftime('%m-%d-%Y %H:%M:%S')if pd.notnull(x) and x != 'unknown' else x)
vh.to_csv('./recursos/vehicles.csv', index=False)
print("Formato de fecha reemplazado correctamente\n")