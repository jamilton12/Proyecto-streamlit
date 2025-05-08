import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Cada filtro debe ser configurable desde la barra lateral (st.sidebar) y aplicarse solo si el usuario lo activa. Los filtros se basarán en las técnicas de filtrado del tutorial (operadores de comparación, lógicos, isin, query, where, mask, str, between, isnull/notnull, fechas). A continuación, se describen los 10 filtros:
""")

st.header('Link Colap')
st.markdown("""
- [Colap Actividad n° 3 parte 1](https://colab.research.google.com/drive/1IZ-xjQd8WUJTwtA1gX9AhL-DE570mwjO#scrollTo=oA5lj938q8i7)
""")

st.header("Solución")

df_nuevo = pd.read_csv('static/datasets/3_M2_Actividad_3/df_nuevo_exportado.csv')

st.subheader("Aplicacion de filtros dinamicos")

activar_filtro_edad = st.sidebar.checkbox('Filtro por rango de edad')

activar_filtro_municipio = st.sidebar.checkbox("Filtrar por municipios")

activar_filtro_ingreso = st.sidebar.checkbox("Filtrar por ingreso mensual mínimo")

activar_filtro_ocupacion = st.sidebar.checkbox("Filtrar por ocupación")

activar_filtro_vivienda = st.sidebar.checkbox("Filtrar personas sin vivienda propia")

activar_filtro_nombre = st.sidebar.checkbox("Filtrar por nombre")

activar_filtro_anio = st.sidebar.checkbox("Filtrar por año de nacimiento")

activar_filtro_internet = st.sidebar.checkbox("Filtrar por acceso a internet")

activar_filtro_ingreso_nulo = st.sidebar.checkbox("Filtrar por ingresos nulos")

activar_filtro_rango_fecha = st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento")

#Aplicar filtro de edad 

if activar_filtro_edad:
    min_edad, max_edad = st.sidebar.slider('Selecciona el rango de edad', 15,75, (28, 40))

    df_nuevo = df_nuevo[df_nuevo['edad'].between(min_edad, max_edad)]

#Aplicar el filtro por municipio 
#Se cogio el arreglo de la configuracioón del escrip que hace el DataFrame 

municipios_opciones = [
            'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
            'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
            'Villavicencio', 'Yopal',                    # Orinoquía
            'Leticia', 'Puerto Inírida'                  # Amazonía
]

if activar_filtro_municipio:
    municipios_seleccionados = st.sidebar.multiselect("Selecciona los municipios", municipios_opciones)

    if municipios_seleccionados:
        df_nuevo = df_nuevo[df_nuevo['municipio'].isin(municipios_seleccionados)]

#Aplicar filtro por ingresos mensuales

if activar_filtro_ingreso:
    ingreso_minimo = st.sidebar.slider("Selecciona el ingreso mínimo (COP)", 800000, 12000000, 2000000, step=100000)

    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'] > ingreso_minimo]

#Aplicar filtro por ocupación


ocupaciones_opciones = [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
]

if activar_filtro_ocupacion:
    ocupaciones_seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones_opciones)

    if ocupaciones_seleccionadas:
        df_nuevo = df_nuevo[df_nuevo['ocupacion'].isin(ocupaciones_seleccionadas)]

#Aplicar filtro por vivivenda propia 

if activar_filtro_vivienda:
    df_nuevo = df_nuevo[~(df_nuevo['tipo_vivienda'] == 'Propia')]

#Aplicar filtro por nombre usando "contains"

if activar_filtro_nombre:
    texto_nombre = st.sidebar.text_input("Ingresa parte del nombre (ej. 'a')")

    if texto_nombre.strip() != "":
        df_nuevo = df_nuevo[df_nuevo['nombre_completo'].str.contains(texto_nombre, case=False, na=False)]

#Aplicar filtro por año 

df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'], errors='coerce')

if activar_filtro_anio:
    anio_actual = datetime.now().year
    anio_max = anio_actual - 15  # 2009
    anio_min = anio_actual - 75  # 1949
    opciones_anios = list(range(anio_min, anio_max + 1))

    anio_seleccionado = st.sidebar.selectbox("Selecciona un año de nacimiento", opciones_anios)

    df_nuevo = df_nuevo[df_nuevo['fecha_nacimiento'].dt.year == anio_seleccionado]

#Aplicar filtro por acceso a internet 

if activar_filtro_internet:
    opcion_internet = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])

    acceso_bool = True if opcion_internet == "Sí" else False

    df_nuevo = df_nuevo[df_nuevo['acceso_internet'] == acceso_bool]


#Aplicar filtros por ingresos nullos 

if activar_filtro_ingreso_nulo:
    df_nuevo = df_nuevo[df_nuevo['ingreso_mensual'].isnull()]

#Aplicar filtros por rango de fechas de nacimiento 

if activar_filtro_rango_fecha:
    # Establecer los límites del rango permitido
    fecha_min = datetime(1949, 1, 1).date()
    fecha_max = datetime(2009, 12, 31).date()

    # Inputs de fecha
    fecha_inicio = st.sidebar.date_input("Fecha de nacimiento desde:", fecha_min, min_value=fecha_min, max_value=fecha_max)
    fecha_fin = st.sidebar.date_input("Hasta:", fecha_max, min_value=fecha_min, max_value=fecha_max)

    # Validar rango y aplicar filtro
    if fecha_inicio <= fecha_fin:
        df_nuevo = df_nuevo[
            df_nuevo['fecha_nacimiento'].between(pd.to_datetime(fecha_inicio), pd.to_datetime(fecha_fin))
        ]
    else:
        st.warning("La fecha de inicio debe ser anterior o igual a la fecha final.")

st.write("Resultado del DataFrame filtrado")
st.dataframe(df_nuevo)