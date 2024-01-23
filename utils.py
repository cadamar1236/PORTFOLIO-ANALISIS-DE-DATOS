import os
import zipfile
import numpy as np
from PIL import Image
from keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr
# Preprocesamiento de imágenes
def cargar_y_preprocesar_imagen(ruta_imagen, tamano=(64, 64)):
    # Cargar la imagen
    imagen = Image.open(ruta_imagen).convert('RGB')
    imagen = imagen.resize(tamano)
    imagen = np.array(imagen)
    imagen = imagen / 255.0 # Normalización
    return imagen

def predecir_imagen(ruta_imagen):
    modelo = load_model('modelo_cats_vs_dogs.keras')
    imagen = cargar_y_preprocesar_imagen(ruta_imagen)
    imagen = np.expand_dims(imagen, axis=0)
    prediccion = modelo.predict(imagen)
    if prediccion[0][0] > 0.5:
        print("Es un perro")
    else:
        print("Es un gato")