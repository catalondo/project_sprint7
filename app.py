import streamlit as st
import pandas as pd
import plotly.express as px

vehicle_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Datos de Vehículos Usados')

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de vehículos usados')
         
         # crear un histograma
    fig = px.histogram(vehicle_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button: # Aquí va el código para crear el gráfico
    st.write('Creación de un gráfico de dispersión para analizar la relación entre la medida de kilometraje y el precio')

fig = px.scatter(vehicle_data, x="odometer", y="price")
st.plotly_chart(fig, use_container_width=True)

import streamlit as st

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
