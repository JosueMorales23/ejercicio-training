import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Precio promedio por año: ")
precioPromedioAño  = vh.groupby(['year', 'model'])['price'].mean().reset_index(name='precioPromedio')
print(precioPromedioAño)
print("--------------------------------------------------------------------------------\n")