import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')
print("Generando diagrama de relacion entre el precio y la condicion del vehiculo...\n")
vh['condition'] = vh['condition'].astype(str)
vh.plot(kind='scatter', x='condition', y='price', ylim=(1, 10))
plt.title("Relacion entre el precio y la condicion")
plt.show()
print("Diagrama generado con exito!\n")
print("Justificacion del grafico en el archivo README\n")