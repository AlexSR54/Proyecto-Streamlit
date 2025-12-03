import streamlit as st
import pandas as pd

# Titulo para la pagina en la pestaña
st.set_page_config(page_title="Registrar datos")
st.title("Registrar y eliminar datos")

# Se repite variable y carga del archivo
archivo = "global_unemployment_data.csv"
try:
    df = pd.read_csv(archivo)
except:
    st.error("No se pudo cargar el archivo.")
    st.stop()

# Titulo de registrar datos
st.header("Registrar datos")

# Selectbox para cada categoría con valores únicos evitando repeticiones
pais = st.selectbox("País", df["country_name"].unique())
sexo = st.selectbox("Sexo", df["sex"].unique())
categoria = st.selectbox("Categoría de edad", df["age_categories"].unique())

# Convertir age_categories en age_group con el fin de que si se agrega un dato con age_categories se agregan ambas columnas
age_map = {
    "Children": "Under 15",
    "Youth": "15-24",
    "Adults": "25+"
}
age_group = age_map[categoria]

# Año
elano = st.number_input("Año", min_value=1900, max_value=2100, step=1, value=2025)
elano_str = str(int(elano))

# Cifras de desempleo
cifra = st.number_input(
    "Tasa de desempleo (%)", 
    min_value=0.0, 
    max_value=100.0, 
    step=0.1
)
# Botón para guardar el registro nuevo
if st.button("Guardar dato"):

    # Esto crea columna del año si no existe esto por medio pd.NA añade valores vacios o digamos en cero hasta que se registre con el nuevo dato, es como reemplazar
    if elano_str not in df.columns:
        df[elano_str] = pd.NA

    # Asegurar que la columna sea numérica
    df[elano_str] = pd.to_numeric(df[elano_str], errors="coerce")

    # 2. Buscar si ya existe fila con esa combinación
    filtro = (
        (df["country_name"] == pais) &
        (df["sex"] == sexo) &
        (df["age_categories"] == categoria)
    )
    # Este if sirve para actualizar el datos si ya existe una fila con la combinación que se filtro anteriormente
    if df[filtro].shape[0] > 0:
        df.loc[filtro, elano_str] = cifra
        mensaje = "Dato actualizado."
        fila_resultado = df[filtro]

    else:
        #En caso de no existir una fila con la combinación previa se crea una nueva fila
        nueva_fila = {
            "country_name": pais,
            "indicator_name": "Unemployment rate by sex and age",
            "sex": sexo,
            "age_group": age_group,
            "age_categories": categoria,
            elano_str: cifra
        }
        # Completar columnas faltantes para que coincida con el CSV
        for col in df.columns:
            if col not in nueva_fila:
                nueva_fila[col] = pd.NA
        # Esto añade la nueva fila al DataFrame pero mantieniedo la logica del dataframe por medio de pd.concat. pd.concat une dataframes = GOD
        df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
        mensaje = "Dato registrado"
        fila_resultado = pd.DataFrame([nueva_fila])

    #Guardar archivo CSV
    df.to_csv(archivo, index=False)
    st.success(mensaje)
    st.dataframe(fila_resultado)

#Titulo de eliminar datos y enunciados
st.header("Eliminar dato")
st.write("Seleccione el índice a eliminar:")
st.dataframe(df)

# Input para el índice a eliminar y botón para eliminar
indice = st.number_input(
    "Índice a eliminar", 
    min_value=0, 
    max_value=len(df) - 1, 
    step=1
)
if st.button("Eliminar"):
    df = df.drop(indice).reset_index(drop=True)
    df.to_csv(archivo, index=False)
    st.success("Dato eliminado.")
    st.dataframe(df)
