import pandas as pd

# Carga de datos
vh = pd.read_csv('./recursos/vehicles.csv')
paint_color = vh['paint_color']

def colorHexadecimal(color):
    if color == 'black':
        return '#000000'
    elif color == 'blue':
        return '#0000FF'
    elif color == 'brown':
        return '#A52A2A'
    elif color == 'green':
        return '#008000'
    elif color == 'grey':
        return '#808080'
    elif color == 'orange':
        return '#FFA500'
    elif color == 'purple':
        return '#800080'
    elif color == 'red':
        return '#FF0000'
    elif color == 'silver':
        return '#C0C0C0'
    elif color == 'white':
        return '#FFFFFF'
    elif color == 'yellow':
        return '#FFFF00'
    else:
        return None

print("Creando columna hexadecimal")
vh['hex_color'] = paint_color.apply(colorHexadecimal)
vh.to_csv('./recursos/vehicles.csv', index=False)
print("Colores creados correctamente\n")
print(vh.head())