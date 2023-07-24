import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Top 10 de modelos mas caros por cada concesionaria: ")
top = vh.groupby('manufacturer').apply(lambda x: x.nlargest(10, ['price'])).reset_index(drop=True)
top = top[['manufacturer', 'model', 'price']]
print(top)
print("--------------------------------------------------------------------------------\n")

print("Top 10 de modelos mas baratos por cada concesionaria: ")
top = vh.groupby('manufacturer').apply(lambda x: x.nsmallest(10, ['price'])).reset_index(drop=True)
top = top[['manufacturer', 'model', 'price']]
print(top)
print("--------------------------------------------------------------------------------\n")

print("Top 10 de modelos mas caros: ")
top = vh.nlargest(10, ['price'])
top = top[['manufacturer', 'model', 'price']]
print(top)
print("--------------------------------------------------------------------------------\n")