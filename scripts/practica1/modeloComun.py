import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Los 10 modelos mas comunes:")
modeloComun = vh['model'].value_counts().head(10).reset_index(name='cantidad')
print(modeloComun)
print("--------------------------------------------------------------------------------\n")

print("Los 10 modelos menos comunes:")
modeloComun = vh['model'].value_counts().tail(10).reset_index(name='cantidad')
print(modeloComun)
print("--------------------------------------------------------------------------------\n")

print("Todos los modelos:")
modeloComun = vh['model'].value_counts().reset_index(name='cantidad')
print(modeloComun)
print("--------------------------------------------------------------------------------\n")