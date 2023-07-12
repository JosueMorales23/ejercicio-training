import pandas as pd

# Carga de datos
vh = pd.read_csv('./resources/vehicles.csv')

print("Reemplazando valores null por el valor de unknown")
vh.fillna('unknown', inplace=True)
vh.to_csv('./ecursos/vehicles.csv', index=False)
print("Valores reemplazados correctamente\n")

print("----------------------------------------------------------------------------------------------------\n")