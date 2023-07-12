import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Top 5 modelos mas baratos de las regiones: ")
top = vh.nsmallest(5, ['price'])
top = top[['region','manufacturer', 'model', 'price']]
print(top)
print("--------------------------------------------------------------------------------\n")

print("Top 5 modelos mas baratos por región: ")
top = vh.groupby('region').apply(lambda x: x.nsmallest(5, ['price'])).reset_index(drop=True)
top = top[['region', 'manufacturer', 'model', 'price']]
print(top)
print("--------------------------------------------------------------------------------\n")