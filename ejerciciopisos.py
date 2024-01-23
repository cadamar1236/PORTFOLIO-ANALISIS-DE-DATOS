import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr

df = pd.read_csv('pisos_precios.csv')
# X son las características (superficie_construida y distritos_id) e Y es lo que queremos predecir (precio)
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']
# Dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(df.head())
print(df.isnull().sum())
print(df['distritos_id'].unique())
print(df.describe())
# X son las características (superficie_construida y distritos_id) e Y es lo que queremos predecir (precio)
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']
# Crea una figura y un conjunto de subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10)) # 2 filas, 2 columnas
# Correlación de Pearson
correlacion = df['superficie_construida'].corr(df['precio'])
print('------- Correlación de Pearson m2 vs precio ------')
print(correlacion)
# Histograma para 'superficie_construida' en la misma escala
# Escalar la superficie para que sea comparable con el precio
scaled_superficie = df['superficie_construida'] * (df['precio'].max() / df['superficie_construida'].max())
# Primer gráfico: Histograma distribución de precios
axs[0, 0].hist(y, bins=50, alpha=0.5, label='Precio')
axs[0, 0].hist(scaled_superficie, bins=50, alpha=0.5, label='Superficie Construida (Escala Ajustada)')
axs[0, 0].set_xlabel('Escala')
axs[0, 0].set_ylabel('Frecuencia')
axs[0, 0].set_title('Distribución de Precio y Superficie Construida (Escala Ajustada)')
axs[0,0].legend()
# Segundo gráfico: Scatter plot de superficie vs precio
# Definir los valores centrales (puede ser la media o la mediana)
centro_x = x['superficie_construida'].median()
centro_y = y.median()
axs[0, 1].scatter(x['superficie_construida'], y)
axs[0, 1].set_xlabel('Superficie')
axs[0, 1].set_ylabel('Precio (M de €)')
axs[0, 1].axhline(y=centro_y, color='r', linestyle='-') # Línea horizontal
axs[0, 1].axvline(x=centro_x, color='r', linestyle='-') # Línea vertical
# Tercer gráfico con la distribución del precio
axs[1, 0].boxplot(y)
axs[1, 0].legend(['Distribución Precio'])
# Histograma bidimensional
limite_inferior_x = df['superficie_construida'].quantile(0.05)
limite_superior_x = df['superficie_construida'].quantile(0.95)
limite_inferior_y = df['precio'].quantile(0.05)
limite_superior_y = df['precio'].quantile(0.95)
#1.Carga de datos
df = pd.read_csv('pisos_precios.csv') # Datos pisos
df_distritos = pd.read_csv('distritos.csv') # Nombres e ids de distrito
# X son las características (superficie_construida y distritos_id) e Y es lo que queremos predecir (precio)
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']
# Cálculo de precio por metro cuadrado
df['precio_m2'] = df['precio'] / df['superficie_construida']
# Eliminar los valores atípicos usando el percentil 99 y 1 para precio m2
df = df[df['precio_m2'] < df['precio_m2'].quantile(0.99)]
df = df[df['precio_m2'] > df['precio_m2'].quantile(0.01)]
# Con los datos limpios volvemos a reasignar x e y
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']
# Normalizar los datos
media_superficie = x['superficie_construida'].mean()
std_superficie = x['superficie_construida'].std()
superficie_normalizada = (df['superficie_construida'] - media_superficie) / std_superficie
# Combinar la superficie normalizada con 'distritos_id' no normalizado
caracteristicas = pd.DataFrame({
'superficie_construida': superficie_normalizada,
'distritos_id': df['distritos_id']
})
precios = (y - y.mean()) / y.std()
# Dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(caracteristicas, precios, test_size=0.2, random_state=42)
# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(x_train, y_train)
# Hacer predicciones en el conjunto de prueba
y_pred = model.predict(x_test)
# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R²: {r2}')
# Mapeo de distritos
distritos = dict(zip( df_distritos['id'],df_distritos['distrito']))
# Crear la lista de opciones para el Dropdown como tuplas (nombre, id)
opciones_distritos = [(nombre, id) for id, nombre in distritos.items()]

def predict_precio(superficie, distrito):
    # Normalizar solo la superficie construida
    superficie_normalizada = (superficie - media_superficie) / std_superficie
    # Convertirlos en un DataFrame de Pandas para la predicción
    datos_prediccion = pd.DataFrame({
    'superficie_construida': [superficie_normalizada],
    'distritos_id': [distrito]
    })
    # Hacer la predicción (sin normalizar el distrito)
    precio_pred_normalizado = model.predict(datos_prediccion)
    # Desnormalizar la predicción del precio para mostrarlo al usuario
    precio_pred = precio_pred_normalizado * y.std() + y.mean()
    precio_formateado = '{:20,d} €'.format(int(precio_pred[0]))
    return precio_formateado

# Crear la interfaz con Gradio
iface = gr.Interface(
fn=predict_precio,
inputs=["number", gr.Dropdown(opciones_distritos)],
outputs="text", # Cambiado a 'text' para permitir una cadena
title="Predicción de Precio de Inmueble",
description="Introduce los metros cuadrados y selecciona el distrito para predecir el precio"
)
# Ejecutar la interfaz
iface.launch(share=True)

