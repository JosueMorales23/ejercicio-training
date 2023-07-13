import csv
import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('vehiculos.db')
cursor = conn.cursor()

# Crear tabla "manufacturer"
cursor.execute('''CREATE TABLE IF NOT EXISTS manufacturer(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL);
                ''')

# Crear tabla "model"
cursor.execute('''CREATE TABLE IF NOT EXISTS model(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                manufacturer_id INTEGER NOT NULL,
                FOREIGN KEY(manufacturer_id) REFERENCES manufacturer(id));
                ''')

# Crear tabla "region"
cursor.execute('''CREATE TABLE IF NOT EXISTS region(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL);
                ''')

# Crear tabla "county"
cursor.execute('''CREATE TABLE IF NOT EXISTS county(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                region_id INTEGER NOT NULL,
                FOREIGN KEY(region_id) REFERENCES region(id));
                ''')

# Crear tabla "type"
cursor.execute('''CREATE TABLE IF NOT EXISTS type(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL);
                ''')

# Crear tabla "vehiculo"
cursor.execute('''CREATE TABLE IF NOT EXISTS vehicle(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                price REAL,
                year INTEGER,
                condition TEXT,
                cylinders TEXT,
                fuel TEXT,
                odometer REAL,
                title_status TEXT,
                transmission TEXT,
                VIN TEXT,
                drive TEXT,
                size TEXT,
                paint_color TEXT,
                image_url TEXT,
                description TEXT,
                state TEXT,
                lat REAL,
                lon REAL,
                posting_date TEXT,
                short_description TEXT,
                hex_color TEXT,
                model_id INTEGER NOT NULL,
                region_id INTEGER NOT NULL,
                county_id INTEGER NOT NULL,
                type_id INTEGER NOT NULL,
                FOREIGN KEY(model_id) REFERENCES model(id),
                FOREIGN KEY(region_id) REFERENCES region(id),
                FOREIGN KEY(county_id) REFERENCES county(id),
                FOREIGN KEY(type_id) REFERENCES type(id)
                );
                ''')

# Leer el archivo CSV con codificación UTF-8
with open('./recursos/vehicles.csv', 'r', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector) # Saltar la primera fila que contiene los nombres de las columnas
    for fila in lector:
        # Insertar los datos en la tabla "manufacturer"
        cursor.execute('''INSERT INTO manufacturer(
                       name
                       ) VALUES(?)''', (fila[4],))

        # Obtener el ID de la última fila insertada en la tabla "manufacturer"
        id_manufacturer = cursor.lastrowid

        # Insertar los datos en la tabla "model"
        cursor.execute('''INSERT INTO model(
                       name,
                       manufacturer_id
                       ) VALUES(?, ?)''', (fila[5], id_manufacturer))
        
        # Obtener el ID de la última fila insertada en la tabla "model"
        id_model = cursor.lastrowid

        # Insertar los datos en la tabla "region"
        cursor.execute('''INSERT INTO region(
                       name
                       ) VALUES(?)''', (fila[1],))

        # Obtener el ID de la última fila insertada en la tabla "region"
        id_region = cursor.lastrowid

        # Insertar los datos en la tabla "county"
        cursor.execute('''INSERT INTO county(
                       name,
                       region_id
                       ) VALUES(?, ?)''', (fila[19], id_region))

        # Obtener el ID de la última fila insertada en la tabla "county"
        id_county = cursor.lastrowid

        # Insertar los datos en la tabla "type"
        cursor.execute('''INSERT INTO type(
                       name
                       ) VALUES(?)''', (fila[15],))
        
        # Obtener el ID de la última fila insertada en la tabla "type"
        id_type = cursor.lastrowid

        # Insertar los datos en la tabla "vehiculo"
        cursor.execute('''INSERT INTO vehicle(
                       price, year, condition, cylinders, fuel, odometer, title_status, 
                       transmission, VIN, drive, size, paint_color, image_url, description, 
                       state, lat, lon, posting_date, short_description, hex_color, model_id, region_id, county_id, type_id
                   ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                   )''', (fila[2], fila[3], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], 
                          fila[12], fila[13], fila[14], fila[16], fila[17], fila[18], fila[20], fila[21], 
                          fila[22], fila[23], fila[24], fila[25], id_model, id_region, id_county, id_type))
conn.commit()
conn.close()
