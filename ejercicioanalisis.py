import pandas as pd
import matplotlib.pyplot as plt
URL = "https://drive.google.com/uc?export=download&id=1-zKKm5aEEabJS01n4vZhE8iiacnXYWGg"
df = pd.read_csv(URL)
print(df.head(15).to_string(index=False))
data_clean = df.dropna().copy()
data_clean['Height'] = data_clean['Height']*2.4
data_clean['Weight'] = data_clean['Weight']*0.453592
#Calcular peso promedio por genero
# Crear un diagrama de caj# Parte 3: Análisis Exploratorio de Datos

# Agrupar datos por género y calcular el peso medio para cada género
peso_medio_por_genero = data_clean.groupby('Gender')['Weight'].mean()

# Crear histogramas de las distribuciones de altura y peso
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(data_clean['Height'], bins=20, color='blue', alpha=0.7)
plt.title('Distribución de Altura')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(data_clean['Weight'], bins=20, color='green', alpha=0.7)
plt.title('Distribución de Peso')
plt.xlabel('Peso (kg)')
plt.ylabel('Frea para comparar la distribución del peso entre géneros')
plt.figure(figsize=(6, 6))
plt.boxplot([data_clean[data_clean['Gender'] == 'Male']['Weight'], 
             data_clean[data_clean['Gender'] == 'Female']['Weight']], 
            labels=['Hombres', 'Mujeres'])
plt.title('Comparación del Peso entre Géneros')
plt.ylabel('Peso (kg)')
plt.show()
# Parte 4: Operaciones Avanzadas

# Calcular los percentiles del peso para cada género
percentiles_peso = data_clean.groupby('Gender')['Weight'].quantile([0.25, 0.5, 0.75])

# Calcular el IMC (Índice de Masa Corporal)
# IMC = peso (kg) / (altura (m))^2
# Suponiendo que data_clean es una copia o un subconjunto de otro DataFrame
# Utilizar .loc para calcular y asignar el IMC
data_clean.loc[:, 'IMC'] = data_clean['Weight'] / (data_clean['Height'] / 100) ** 2

# Clasificar a los individuos según su IMC
# Bajo Peso: IMC < 18.5, Peso Normal: 18.5 <= IMC < 25
# Sobrepeso: 25 <= IMC < 30, Obesidad: IMC >= 30
condiciones = [
    (data_clean['IMC'] < 18.5),
    (data_clean['IMC'] >= 18.5) & (data_clean['IMC'] < 25),
    (data_clean['IMC'] >= 25) & (data_clean['IMC'] < 30),
    (data_clean['IMC'] >= 30)
]
categorias = ['Bajo Peso', 'Peso Normal', 'Sobrepeso', 'Obesidad']
# Utilizar .loc para asignar la clasificación de IMC
data_clean['Clasificacion_IMC'] = pd.cut(data_clean['IMC'], bins=[0, 18.5, 25, 30, float('inf')], labels=categorias, include_lowest=True)

percentiles_peso, data_clean.head()
