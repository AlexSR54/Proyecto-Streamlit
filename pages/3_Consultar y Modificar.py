import streamlit as st
import pandas as pd

# Titulo para la pagina en la pestaña
st.set_page_config(page_title="Buscar y consultar")
st.title("Buscar y consultar datos")

# Se repite variable y carga del archivo
archivo = "global_unemployment_data.csv"
try:
    df = pd.read_csv(archivo)
except:
    st.error("No se pudo cargar el archivo.")
    st.stop()

# Busqueda de país por medio de un selectbox que almacena los paises unicos en una variable y los compara
paises = df["country_name"].unique()
pais = st.selectbox("País", paises)
resultado = df[df["country_name"] == pais]
st.subheader("Buscar por país")
st.dataframe(resultado)

# Bsuqueda por índice por medio de un input
st.subheader("Buscar por índice")
indice = st.number_input(
    "Índice de fila", 
    min_value=0, 
    max_value=len(df) - 1, 
    step=1
)
st.dataframe(df.loc[[indice]])
