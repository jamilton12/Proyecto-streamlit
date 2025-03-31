import streamlit as st
import pandas as pd
import sqlite3 as sql 
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide",
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Creacion de Dataframes")

st.subheader("Dataframes con Diccionarios")
st.expander("DataFrame con Diccionarios", expanded=False).code("""
import streamlit as st
import pandas as pd

# Crear diccionario con datos sobre libros
datos_libros = {
    "título": ["Cien años de soledad", "1984", "El principito", "Orgullo y prejuicio"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Jane Austen"],
    "año de publicación": [1967, 1949, 1943, 1813],
    "género": ["Realismo mágico", "Distopía", "Fábula", "Novela romántica"]
}

# Convertir diccionario a DataFrame
libros_df = pd.DataFrame(datos_libros)

# Mostrar en Streamlit
st.write("### DataFrame de Libros")
st.dataframe(libros_df)
""")

datos_libros = {
    "título": ["Cien años de soledad", "1984", "El principito", "Orgullo y prejuicio"],
    "autor": ["Gabriel García Márquez", "George Orwell", "Antoine de Saint-Exupéry", "Jane Austen"],
    "año de publicación": [1967, 1949, 1943, 1813],
    "género": ["Realismo mágico", "Distopía", "Fábula", "Novela romántica"]
}

libros_df = pd.DataFrame(datos_libros)

st.write("### DataFrame de Libros")
st.dataframe(libros_df)

st.subheader("Dataframes con Listas de Diccionarios")
st.expander("DataFrame con Listas de Diccionarios", expanded=False).code("""
import streamlit as st
import pandas as pd

# Crear lista de diccionarios con datos de ciudades
ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Buenos Aires", "población": 3075646, "país": "Argentina"},
    {"nombre": "Madrid", "población": 3223334, "país": "España"}
]

# Convertir lista de diccionarios a DataFrame
ciudades_df = pd.DataFrame(ciudades)

# Mostrar en Streamlit
st.write("### Información de Ciudades")
st.dataframe(ciudades_df)
""")

ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Buenos Aires", "población": 3075646, "país": "Argentina"},
    {"nombre": "Madrid", "población": 3223334, "país": "España"}
]

ciudades_df = pd.DataFrame(ciudades)
st.write("### Información de Ciudades")
st.dataframe(ciudades_df)

st.subheader("Dataframes con Listas de Listas")
st.expander("DataFrame con Listas de Listas", expanded=False).code("""
import streamlit as st
import pandas as pd

# Lista de listas representando productos en inventario
productos = [
    ["Laptop", 1200, 15],
    ["Teléfono móvil", 800, 30],
    ["Tablet", 450, 25],
    ["Auriculares inalámbricos", 150, 40]
]

# Definir nombres de columnas
columnas = ["Producto", "Precio", "Cantidad en Stock"]

# Convertir lista de listas en DataFrame
productos_df = pd.DataFrame(productos, columns=columnas)

# Mostrar en Streamlit
st.write("### Productos en Inventario")
st.dataframe(productos_df)
""")

productos = [
    ["Laptop", 1200, 15],
    ["Teléfono móvil", 800, 30],
    ["Tablet", 450, 25],
    ["Auriculares inalámbricos", 150, 40]
]

columnas = ["Producto", "Precio", "Cantidad en Stock"]
productos_df = pd.DataFrame(productos, columns=columnas)

st.write("### Productos en Inventario")
st.dataframe(productos_df)

st.subheader('Dataframes con "Series" ')
st.expander("DataFrame con Series", expanded=False).code("""
import streamlit as st
import pandas as pd

# Crear Series individuales
nombres = pd.Series(["Ana", "Luis", "Carlos", "María"])
edades = pd.Series([28, 34, 23, 45])
ciudades = pd.Series(["Bogotá", "Lima", "Quito", "Santiago"])

# Combinar Series en un diccionario
datos_personas = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

# Convertir diccionario en DataFrame
personas_df = pd.DataFrame(datos_personas)

# Mostrar en Streamlit
st.write("### Datos de Personas")
st.dataframe(personas_df)
""")

nombres = pd.Series(["Ana", "Luis", "Carlos", "María"])
edades = pd.Series([28, 34, 23, 45])
ciudades = pd.Series(["Bogotá", "Lima", "Quito", "Santiago"])

datos_personas = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

personas_df = pd.DataFrame(datos_personas)

st.write("### Datos de Personas")
st.dataframe(personas_df)

st.subheader('Dataframes con Archivo CSV (local) ')
st.expander("DataFrame con Archivo CSV (local)", expanded=False).code("""
import streamlit as st
import pandas as pd

csv_df = pd.read_csv("data.csv")

# Mostrar en Streamlit
st.write("### Datos desde CSV")
st.dataframe(csv_df)
""")

csv_df = pd.read_csv("assets/1_M2_Actividad_1/dataCSV.csv")

st.write("### Datos desde CSV")
st.dataframe(csv_df)

st.subheader('Dataframes con Archivo Excel (local) ')
st.expander("DataFrame con Archivo Excel (local)", expanded=False).code("""
import streamlit as st
import pandas as pd

# Leer archivo Excel desde ruta local
excel_df = pd.read_excel("data.xlsx", engine="openpyxl")

# Mostrar en Streamlit
st.write("### Datos desde Excel")
st.dataframe(excel_df)
""")

excel_df = pd.read_excel("assets/1_M2_Actividad_1/dataExcel.xlsx", engine="openpyxl")

st.write("### Datos desde Excel")
st.dataframe(excel_df)

st.subheader('Dataframes con Archivo JSON (local) ')
st.expander("DataFrame con Archivo JSON (local)", expanded=False).code("""
import streamlit as st
import pandas as pd

# Leer archivo JSON desde ruta local
json_df = pd.read_json("data.json")

# Mostrar en Streamlit
st.write("### Datos de Usuarios desde JSON")
st.dataframe(json_df)
""")

json_df = pd.read_json("assets/1_M2_Actividad_1/dataJSON.json")

st.write("### Datos de Usuarios desde JSON")
st.dataframe(json_df)

st.subheader('Dataframes con Archivo CSV (online) ')
st.expander("DataFrame con Archivo CSV (online)", expanded=False).code("""
import streamlit as st
import pandas as pd

# Leer CSV desde URL
url_csv = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_online = pd.read_csv(url_csv)

# Mostrar en Streamlit
st.write("### Datos desde URL")
st.dataframe(df_online)
""")

url_csv = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df_online = pd.read_csv(url_csv)

st.write("### Datos desde URL")
st.dataframe(df_online)

st.subheader('Dataframes con Base de datos SQLite')
st.expander("DataFrame con Base de datos SQLite", expanded=False).code("""
import streamlit as st
import pandas as pd
import sqlite3

# Crear y conectar a una base SQLite llamada estudiantes.db
conn = sqlite3.connect('estudiantes.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    calificacion REAL
)
''')

# Insertar datos (solo ejecutar una vez para evitar duplicados)
cursor.executemany('INSERT INTO estudiantes (nombre, calificacion) VALUES (?,?)', [
    ('Ana Gómez', 89.5),
    ('Luis Pérez', 76.0),
    ('María Rodríguez', 93.5)
])

# Confirmar cambios y cerrar cursor
conn.commit()

# Consultar datos con Pandas
df_estudiantes = pd.read_sql('SELECT * FROM estudiantes', conn)

# Cerrar conexión
conn.close()

# Mostrar en Streamlit
st.write("### Datos desde SQLite")
st.dataframe(df_estudiantes
""")

conn = sql.connect('estudiantes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    calificacion REAL
)
''')

cursor.execute('SELECT COUNT(*) FROM estudiantes')
if cursor.fetchone()[0] == 0:
    cursor.executemany('INSERT INTO estudiantes (nombre, calificacion) VALUES (?,?)', [
        ('Ana Gómez', 89.5),
        ('Luis Pérez', 76.0),
        ('María Rodríguez', 93.5)
    ])
    conn.commit()

df_estudiantes = pd.read_sql('SELECT * FROM estudiantes', conn)

conn.close()

st.write("### Datos desde SQLite")
st.dataframe(df_estudiantes)

st.subheader('Dataframes con Array de NumPy')
st.expander("DataFrame con Array de NumPy", expanded=False).code("""
import streamlit as st
import pandas as pd
import numpy as np

# Crear un array bidimensional con NumPy
data_numpy = np.array([
    [101, "Carlos", 88.5],
    [102, "Sofía", 92.0],
    [103, "Andrés", 77.5]
])

# Convertir el array de NumPy en DataFrame
numpy_df = pd.DataFrame(data_numpy, columns=["ID", "Nombre", "Calificación"])

# Mostrar en Streamlit
st.write("### Datos desde NumPy")
st.dataframe(numpy_df)
""")

data_numpy = np.array([
    [101, "Carlos", 88.5],
    [102, "Sofía", 92.0],
    [103, "Andrés", 77.5]
])

numpy_df = pd.DataFrame(data_numpy, columns=["ID", "Nombre", "Calificación"])

st.write("### Datos desde NumPy")
st.dataframe(numpy_df)