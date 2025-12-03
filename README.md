# Proyecto-Streamlit
Proyecto Streamlit Técnicas de programación 
Este proyecto es una aplicación desarrollada en Python usando Streamlit. Permite trabajar con el archivo global_unemployment_data.csv para registrar datos, consultarlos, filtrarlos y generar gráficos simples.

## Contenido del proyecto

- Inicio.py  
- global_unemployment_data.csv  
- Carpeta pages/ con las siguientes páginas:
  - 1_Registrar_datos.py
  - 2_Buscar_y_consultar.py
  - 3_Filtros_y_graficos.py
  - 4_Estadisticas.py

## Funcionalidades

1. Registrar datos:
   - Añadir un nuevo registro
   - Eliminar una fila por índice

2. Consultar y modificar:
   - Buscar por país
   - Consultar una fila por índice

3. Filtros y gráficos:
   - Filtrar por país, sexo y categoría de edad
   - Gráficos de línea, barras y dispersión

4. Estadísticas:
   - Promedio anual del país
   - Comparación por sexo
   - Comparación por grupos de edad

## Requisitos

- Python 3.10 o superior
- Librerías: streamlit, pandas, matplotlib

## Ejecución

En la terminal, ejecutar:

streamlit run Inicio.py
