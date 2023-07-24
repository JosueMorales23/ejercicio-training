import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')

columnaNueva = input("Desea agregar la columna short_description? (s/n):")
if columnaNueva.lower() == 's':
    if 'short_description' not in vh.columns:
        # Agregar la nueva columna "short_description"
        vh = vh.assign(short_description=vh['manufacturer'] + ' ' + vh['model'] 
                            + ' - ' + vh['region'] + ' - ' + vh['cylinders'] + ' - ' + vh['title_status'])
        respuesta = input('¿Desea guardar los datos en el archivo original? (s/n): ')
        if respuesta.lower() == 's':
            vh.to_csv('./recursos/vehicles.csv', index=False)
            print(vh.info())
        else:
            vh.to_csv('./recursos/vehiclesNew.csv', index=False)
            vhNew = pd.read_csv('./recursos/vehiclesNew.csv')
            print(vhNew.info())
    else:
        print("La columna short_description ya existe")
else:
    print("No se agregará la columna short_description\n")

print("----------------------------------------------------------------------------------------------------\n")