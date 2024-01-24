import os
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from utils import cargar_y_preprocesar_imagen, predecir_imagen
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Rutas a las carpetas de gatos y perros
ruta_gatos = 'C:\\Users\\Admin\\Desktop\\Ejercicios\\Ejerciciosai\\Cat'
ruta_perros = 'C:\\Users\\Admin\\Desktop\\Ejercicios\\Ejerciciosai\\Dog'
# Cargar y preprocesar imágenes
imagenes = []
etiquetas = []
# Cargar gatos
for archivo in os.listdir(ruta_gatos):
    ruta_completa = os.path.join(ruta_gatos, archivo)
    # Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.jpeg', '.png', '.bmp']
    _, extension = os.path.splitext(archivo)
    # otra opción podría ser ruta_imagen[-4:].lower() para obtener la extensión pero mejor así.
    # Comprobar que la extensión es una de las permitidas
    if (extension.lower() in extensiones_permitidas):
        try:
            img = cargar_y_preprocesar_imagen(ruta_completa)
            imagenes.append(img)
            etiquetas.append(0) # 0 para gatos
        except:
            print(f"No se pudo cargar la imagen {archivo}")
    else:
        continue
# Cargar perros
for archivo in os.listdir(ruta_perros):
    ruta_completa = os.path.join(ruta_perros, archivo)
    # Lista de extensiones permitidas
    extensiones_permitidas = ['.jpg', '.jpeg', '.png', '.bmp']
    _, extension = os.path.splitext(archivo)
    # otra opción podría ser ruta_imagen[-4:].lower() para obtener la extensión pero mejor así.
    # Comprobar que la extensión es una de las permitidas
    if (extension.lower() in extensiones_permitidas):
        try:
            img = cargar_y_preprocesar_imagen(ruta_completa)
            imagenes.append(img)
            etiquetas.append(1) # 1 para perros
        except:
            print(f"No se pudo cargar la imagen {archivo}")
    else:
        continue
# Convertir listas a arrays de Numpy
imagenes = np.array(imagenes)
etiquetas = np.array(etiquetas)
X_train, X_test, y_train, y_test = train_test_split(imagenes, etiquetas,
test_size=0.2, random_state=42)
# Construcción del modelo
modelo = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])
# Compilación del modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
modelo.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
# Evaluar el modelo
evaluacion = modelo.evaluate(X_test, y_test)
print(f"Test Accuracy: {evaluacion[1] * 100}%")
modelo.save('modelo_cats_vs_dogs.keras') # Guarda el modelo en un archivo .keras
modelo = load_model('modelo_cats_vs_dogs.keras')
predecir_imagen('perro1.jpg')
predecir_imagen('perro2.jpg')
predecir_imagen('gato1.jpg')
predecir_imagen('gato2.jpg')

