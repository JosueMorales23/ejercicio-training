import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

print("Eliminacion de columnas")
while True:
    for i,columnas in enumerate (vh.columns):
        print(i+1, columnas)
    columna_a_eliminar = int(input("Ingrese el número de la columna a eliminar: "))
    print("Eliminando columna...")
    vh.drop(vh.columns[columna_a_eliminar-1], axis=1, inplace=True)
    vh.to_csv('./recursos/vehicles.csv', index=False)
    print("La columna se ha eliminado correctamente\n")
    respuesta = input('¿Desea seguir eliminando columnas? (s/n): ')
    if respuesta.lower() != 's':
        break

print("----------------------------------------------------------------------------------------------------\n")