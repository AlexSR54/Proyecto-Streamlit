import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Titulo para la pagina en la pestaña
st.set_page_config(page_title="Estadísticas")
st.title("Estadísticas")

# Se repite variable y carga del archivo
archivo = "global_unemployment_data.csv"
try:
    df = pd.read_csv(archivo)
except:
    st.error("No se pudo cargar el archivo")
    st.stop()

# Selección del país
pais = st.selectbox("País", df["country_name"].unique())
datos = df[df["country_name"] == pais]
st.dataframe(datos)

# Este es un filtro para obtener las columnas que son años y no columnas que contengan texto
elanos = [c for c in df.columns if c.isnumeric()]

# Promedio anual del país
st.subheader("Promedio anual")
prom = datos[elanos].mean()
# Gráfico de línea
fig1, ax1 = plt.subplots()
ax1.plot(elanos, prom)
ax1.set_xlabel("Año")
ax1.set_ylabel("Porcentaje")
st.pyplot(fig1)

# Promedio por sexo
st.subheader("Promedio por sexo")
sexos = ["Male", "Female"]
prom_sexo = {}

for s in sexos:
    d = datos[datos["sex"] == s]
    prom_sexo[s] = d[elanos].mean().mean()
# Gráfico de barras
fig2, ax2 = plt.subplots()
ax2.bar(prom_sexo.keys(), prom_sexo.values())
ax2.set_ylabel("Porcentaje")
st.pyplot(fig2)

# Promedio por edad
st.subheader("Promedio por categoría de edad")
edades = ["Children", "Youth", "Adults"]
prom_edad = {}
for e in edades:
    d = datos[datos["age_categories"] == e]
    prom_edad[e] = d[elanos].mean().mean()
# Gráfico de barras
fig3, ax3 = plt.subplots()
ax3.bar(prom_edad.keys(), prom_edad.values())
ax3.set_ylabel("Porcentaje")
st.pyplot(fig3)
