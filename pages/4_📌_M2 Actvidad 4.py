import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

st.header("Descripción de la actividad")
st.markdown("""
Creación de una aplicación interactiva con Streamlit utilizando .loc y .iloc
Desarrollar una aplicación web interactiva utilizando Streamlit que permita a los usuarios explorar y manipular un DataFrame de Pandas, haciendo uso intensivo de los métodos .loc y .iloc para realizar selecciones, filtros y modificaciones de datos. La temática y el diseño de la aplicación son libres, permitiendo expresar su creatividad.

## Instrucciones generales:

- Desarrolar la actividad en el archivo 📌_M2_Actividad_4.py del proyecto integrador.
""")

st.header("Solución")

df = pd.read_csv('static/datasets/3_M2_Actividad_3/df_nuevo_exportado.csv')

with st.expander('static/datasets/3_M2_Actividad_3/df_nuevo_exportado.csv'):
    st.dataframe(df)

st.sidebar.header("🔧 Opciones de selección")

# --------------------------
# Selección con .loc
# --------------------------

st.subheader("🔹 Selección con `.loc` (por etiquetas)")

columnas_disponibles = df.columns.tolist()
columna_loc = st.sidebar.selectbox("Selecciona una columna para ver (con .loc)", columnas_disponibles)
fila_inicio_loc = st.sidebar.number_input("Fila inicial (loc)", 0, len(df) - 1, 0)
fila_fin_loc = st.sidebar.number_input("Fila final (loc)", fila_inicio_loc + 1, len(df), fila_inicio_loc + 5)

if st.sidebar.button("Mostrar selección con .loc"):
    st.write(f"Mostrando filas {fila_inicio_loc}:{fila_fin_loc} y columna '{columna_loc}' usando `.loc`:")
    st.dataframe(df.loc[fila_inicio_loc:fila_fin_loc - 1, columna_loc])


# --------------------------
# Selección con .iloc
# --------------------------

st.subheader("🔸 Selección con `.iloc` (por posición)")

fila_inicio_iloc = st.sidebar.number_input("Fila inicial (iloc)", 0, len(df) - 1, 0, key="fila_iloc")
fila_fin_iloc = st.sidebar.number_input("Fila final (iloc)", fila_inicio_iloc + 1, len(df), fila_inicio_iloc + 5, key="fin_iloc")
columna_inicio_iloc = st.sidebar.number_input("Columna inicial (iloc)", 0, len(df.columns) - 1, 0)
columna_fin_iloc = st.sidebar.number_input("Columna final (iloc)", columna_inicio_iloc + 1, len(df.columns), columna_inicio_iloc + 3)

if st.sidebar.button("Mostrar selección con .iloc"):
    st.write(f"Mostrando filas {fila_inicio_iloc}:{fila_fin_iloc} y columnas {columna_inicio_iloc}:{columna_fin_iloc} usando `.iloc`:")
    st.dataframe(df.iloc[fila_inicio_iloc:fila_fin_iloc, columna_inicio_iloc:columna_fin_iloc])

# --------------------------
# Edición con .loc
# --------------------------

st.subheader("✏️ Modificar un valor usando `.loc`")

fila_editar = st.number_input("Fila a editar", 0, len(df) - 1, 0)
columna_editar = st.selectbox("Columna a editar", columnas_disponibles, index=0)
valor_actual = df.loc[fila_editar, columna_editar]
nuevo_valor = st.text_input(f"Ingrese nuevo valor para fila {fila_editar}, columna '{columna_editar}'", str(valor_actual))

if st.button("Aplicar cambio con .loc"):
    df.loc[fila_editar, columna_editar] = nuevo_valor
    st.success(f"Valor actualizado exitosamente en fila {fila_editar}, columna '{columna_editar}'")
    st.dataframe(df.loc[[fila_editar]])

# --------------------------
# Guardar cambios
# --------------------------
csv = df.to_csv(index=False)
buffer = io.BytesIO()
buffer.write(csv.encode('utf-8'))
buffer.seek(0)

# Botón para descargar el archivo
st.download_button(
    label="⬇️ Descargar CSV actualizado",
    data=buffer,
    file_name="df_nuevo_actualizado.csv",
    mime="text/csv"
)