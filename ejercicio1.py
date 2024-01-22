import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
os.getcwd()
# Cargar el dataset en un DataFrame de Pandas
df = pd.read_csv("IMDB-Movie-Data.csv")

# Seleccionar columnas relevantes
selected_columns = ['Title', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']
df = df[selected_columns]

# Paso 2: Convertir columnas a un array de Numpy
numpy_array = df.to_numpy()

# Paso 3: Manejar valores faltantes en 'Revenue (Millions)'
mean_revenue = df['Revenue (Millions)'].mean()
df['Revenue (Millions)'].fillna(mean_revenue, inplace=True)

# Análisis Estadístico con Numpy
# Calcular la calificación promedio de las películas
average_rating = np.mean(numpy_array[:, 3])

# Encontrar la película con la duración más larga
longest_movie_duration = np.max(numpy_array[:, 2])
longest_movie_title = df[df['Runtime (Minutes)'] == longest_movie_duration]['Title'].values[0]

# Calcular el ingreso promedio y la mediana de los ingresos de las películas
average_revenue = np.mean(numpy_array[:, 5])
median_revenue = np.median(numpy_array[:, 5])

# Paso 4: Manipulación de Datos
# Crear un subconjunto de datos con películas lanzadas en los últimos 10 años
recent_movies_subset = df[df['Year'] >= (df['Year'].max() - 10)]

# Calcular el promedio de votos para este subconjunto
average_votes_recent_movies = np.mean(recent_movies_subset['Votes'])

# Paso 5: Correlación
# Calcular la correlación entre la calificación de IMDb y los ingresos de las películas
# correlation = np.corrcoef(numpy_array[:, 3], numpy_array[:, 5])[0, 1]

# Representar la correlación con matplotlib
plt.scatter(numpy_array[:, 3], numpy_array[:, 5])
plt.xlabel('IMDb Rating')
plt.ylabel('Revenue (Millions)')
plt.title('Correlación entre Calificación IMDb e Ingresos')
plt.show()

# Imprimir resultados
print(f"Calificación promedio de las películas: {average_rating}")
print(f"Película con la duración más larga: {longest_movie_title} ({longest_movie_duration} minutos)")
print(f"Ingreso promedio de las películas: {average_revenue} millones")
print(f"Mediana de ingresos de las películas: {median_revenue} millones")
print(f"Promedio de votos para películas lanzadas en los últimos 10 años: {average_votes_recent_movies}")