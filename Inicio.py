import streamlit as st
import pandas as pd

# Titulo para la pagina en la pestaña
st.set_page_config(page_title="Proyecto Python")

# Titulos de la pagina principal y texto
st.title("Pagina Principal")
st.write("Bienevido a la app de desempleo, aquí veras estadísticas mundiales sobre el desempleo por país y año :)")

# Imagen de la pagina principal
st.image('assets/Imagen Pagina Principal.png', width=700)

# Se usa esta variable que indica el nombre del archivo a cargar ya que es el unico archivo a trabajar con este codigo
archivo = "global_unemployment_data.csv"

# Cargar la base de datos y en caso de no subirse marcar error
try:
    df = pd.read_csv(archivo)
    st.success("Archivo cargado.")
except:
    st.error(f"No se pudo cargar el archivo '{archivo}'.")
    st.stop()

# Previsualización de la base de datos 
st.subheader("Vista previa del archivo:")
st.dataframe(df.head())
