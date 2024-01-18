import pandas as pd
# 1. Crear una Serie de Pandas a partir de una lista de números.
lista_numeros = [1, 2, 3, 4, 5]
serie = pd.Series(lista_numeros)
# 2. Mostrar la Serie.
print("Serie original:")
print(serie)
# 5. Realizar operaciones aritméticas básicas en toda la Serie.
suma = serie.sum()
resta = serie.subtract(2)  # Restar 2 a cada elemento
multiplicacion = serie.multiply(3)  # Multiplicar cada elemento por 3
division = serie.divide(2)  # Dividir cada elemento por 2

# 6. Mostrar los resultados de cada operación.
print("\nResultados:")
print(f"Suma: {suma}")
print(f"Resta (restar 2 a cada elemento):\n{resta}")
print(f"Multiplicación (multiplicar por 3):\n{multiplicacion}")
print(f"División (dividir por 2):\n{division}")
