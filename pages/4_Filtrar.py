import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titulo para la pagina en la pestaña
st.set_page_config(page_title="Filtros y Gráficos")
st.title("Filtros y Gráficos")

# Se repite variable y carga del archivo
archivo = "global_unemployment_data.csv"
try:
    df = pd.read_csv(archivo)
except:
    st.error("No se pudo cargar el archivo")
    st.stop()

# Quitar espacios en columnas, lo mejor que pudo existir
df.columns = df.columns.str.strip()

# Filtros con unique para solo buscar datos unicos
pais = st.selectbox("País", df["country_name"].unique())
sexo = st.selectbox("Sexo", df["sex"].unique())
edad = st.selectbox("Categoría de edad", df["age_categories"].unique())

# Filtrar de datos
filtro = df[
    (df["country_name"] == pais) &
    (df["sex"] == sexo) &
    (df["age_categories"] == edad)
]
st.subheader("Datos filtrados")
st.dataframe(filtro)

# Años - if not sirve para evitar errores si el filtro no tiene datos "Mera chimba"
años = [c for c in df.columns if c.isdigit()]
if not filtro.empty:
    fila = filtro.iloc[0]
    valores = fila[años]

    # Gráfico de línea
    st.subheader("Gráfico de línea")
    fig1, ax1 = plt.subplots()
    ax1.plot(años, valores)
    ax1.set_xlabel("Año")
    ax1.set_ylabel("Porcentaje")
    st.pyplot(fig1)

    # Gráfico de barras
    st.subheader("Gráfico de barras")
    fig2, ax2 = plt.subplots()
    ax2.bar(años, valores)
    ax2.set_xlabel("Año")
    ax2.set_ylabel("Porcentaje")
    st.pyplot(fig2)

    # Gráfico de dispersión
    st.subheader("Gráfico de dispersión")
    fig3, ax3 = plt.subplots()
    ax3.scatter(años, valores)
    ax3.set_xlabel("Año")
    ax3.set_ylabel("Porcentaje")
    st.pyplot(fig3)

