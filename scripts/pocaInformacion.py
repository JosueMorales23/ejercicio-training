import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Borra filas con menos del 50 de datos")
cantidad = len(vh.columns) * 0.5
datosBorrar = vh[vh.isna().sum(axis=1) >= cantidad]

print("Se van a borar", len(datosBorrar), "filas")
print(datosBorrar[['id', 'manufacturer', 'model']])
print("Borrando...")
vh.dropna(thresh=cantidad, inplace=True)
vh.to_csv('./recursos/vehicles.csv', index=False)
print("Valores reemplazados correctamente\n")
