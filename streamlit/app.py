import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.header('Anuncios de Venta de Coches')

""" Botón para construir histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price", color="condition")
    st.plotly_chart(fig, use_container_width=True)"""

# Casilla de verificación para construir histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación para construir gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="year", y="price", color="condition")
    st.plotly_chart(fig, use_container_width=True)
