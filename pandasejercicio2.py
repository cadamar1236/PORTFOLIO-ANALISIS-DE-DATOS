import pandas as pd

# Paso 1: Crear dos Series de Pandas a partir de listas de datos
temperaturas = [25, 28, 30, 24, 22, 26, 29]
precipitacion = [5, 10, 2, 15, 8, 3, 7]

serie_a = pd.Series(temperaturas, name='Temperaturas (°C)')
serie_b = pd.Series(precipitacion, name='Precipitación (mm)')

# Paso 2: Realizar operaciones de slicing en ambas Series
slicing_a = serie_a[2:5]  # Slicing en la Serie A
slicing_b = serie_b[:3]   # Slicing en la Serie B

# Paso 3: Combinar las Series resultantes del slicing en una nueva Serie
serie_combinada = pd.concat([slicing_a, slicing_b], axis=0)

# Paso 4: Realizar operaciones básicas en la Serie combinada
promedio = serie_combinada.mean()
maximo = serie_combinada.max()
minimo = serie_combinada.min()

# Imprimir los resultados
print("Serie A:")
print(serie_a)
print("\nSerie B:")
print(serie_b)
print("\nSlicing Serie A:")
print(slicing_a)
print("\nSlicing Serie B:")
print(slicing_b)
print("\nSerie Combinada:")
print(serie_combinada)
print("\nPromedio de la Serie Combinada:", promedio)
print("Máximo de la Serie Combinada:", maximo)
print("Mínimo de la Serie Combinada:", minimo)
