import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Cantidad registrada por año")
grupoYear = vh.groupby(['year']).size().reset_index(name='cantidad')
print(grupoYear)
print("--------------------------------------------------------------------------------\n")

print("Cantidad registrada por región")
grupoRegion = vh.groupby(['region']).size().reset_index(name='cantidad')
print(grupoRegion)
print("--------------------------------------------------------------------------------\n")

print("Cantidad registrada por fabricante")
grupoManufacturer = vh.groupby(['manufacturer']).size().reset_index(name='cantidad')
print(grupoManufacturer)
print("--------------------------------------------------------------------------------\n")