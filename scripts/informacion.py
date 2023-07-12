import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Uso de head para ver las primeras filas")
print(vh.head())

print("----------------------------------------------------------------------------------------------------\n")
print("Uso de tail para ver las últimas filas")
print(vh.tail())

print("----------------------------------------------------------------------------------------------------\n")
print("Uso de info para ver el tipo de datos de cada columna")
print(vh.info())

print("----------------------------------------------------------------------------------------------------\n")
print("Uso de describe para ver estadísticas de las columnas numéricas")
print(vh.describe())

print("----------------------------------------------------------------------------------------------------\n")