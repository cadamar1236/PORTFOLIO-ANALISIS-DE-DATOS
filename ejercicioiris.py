# Importar TensorFlow y otros paquetes
import tensorflow as tf
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
iris = datasets.load_iris()
print(iris)
X = iris.data
y = iris.target
# Codificar las etiquetas utilizando OneHotEncoder antes de dividir los datos
encoder = OneHotEncoder(sparse=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train_encoded, y_test_encoded = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Normalizar los datos (opcional, dependiendo del modelo)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Crear el modelo de red neuronal

model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
# Entrenar el modelo
model.fit(X_train, y_train_encoded, epochs=50, batch_size=32, validation_split=0.2)

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test_encoded)
print(f'\nAccuracy en el conjunto de prueba: {accuracy}')
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)

# Comparar con las etiquetas conocidas
print('\nEtiquetas reales:', np.argmax(y_test_encoded, axis=1))
print('Etiquetas predichas:', predicted_classes)
print("La clase predicha para las nuevas flores de Iris son:", iris.target_names[predicted_classes])
#Ejemplo
new_data = np.array([[5.1, 3.5, 1.4, 0.2]])
predictions_1 = model.predict(new_data)
predictions_2 = np.argmax(predictions_1, axis=1)
print("La clase predicha para el ejemplo de flores de Iris es:", iris.target_names[predictions_2])