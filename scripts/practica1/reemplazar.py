import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Reemplazando valores null por el valor de unknown")
vh.fillna('unknown', inplace=True)
vh.to_csv('./recursos/vehicles.csv', index=False)
print("Valores reemplazados correctamente\n")

print("----------------------------------------------------------------------------------------------------\n")