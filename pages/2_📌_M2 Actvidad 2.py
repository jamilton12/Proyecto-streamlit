import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

st.header("Exploración de datos con Pandas")

# Título de la app
st.title("Análisis de Estudiantes de Colombia")

# Cargar los datos
df = pd.read_csv('static/datasets/2_M2_Actividad_2/dataEstudiante.csv')

# Mostrar las primeras 5 filas y las últimas 5 filas
if st.checkbox("Ver primeras 5 filas"):
    st.write(df.head())

if st.checkbox("Ver últimas 5 filas"):
    st.write(df.tail())

# Mostrar un resumen con .info() y .describe()
if st.checkbox("Resumen de .info()"):
    st.write(df.info())

if st.checkbox("Resumen de .describe()"):
    st.write(df.describe())

# Seleccionar columnas específicas
columnas_seleccionadas = st.multiselect("Selecciona las columnas para mostrar", df.columns)
if columnas_seleccionadas:
    st.write(df[columnas_seleccionadas])

# Filtrar estudiantes por promedio
valor_promedio = st.slider("Selecciona el promedio mínimo", min_value=0.0, max_value=5.0, step=0.1, value=3.0)
df_filtrado = df[df["promedio"] > valor_promedio]

# Mostrar el dataframe filtrado
st.write(f"Estudiantes con promedio mayor a {valor_promedio}:", df_filtrado)