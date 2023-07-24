import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Cantidad por modelo")
cantidadModelo = vh.groupby(['model']).size().reset_index(name='cantidad')
cantidadModeloOrdenada = cantidadModelo.sort_values(by=['cantidad'], ascending=False)
print(cantidadModeloOrdenada)
print("--------------------------------------------------------------------------------\n")