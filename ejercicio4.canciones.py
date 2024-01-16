import random

# Listas de canciones y duraciones en minutos
canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01] 

# Combinar las dos listas en un diccionario
diccionario_canciones = dict(zip(canciones, duraciones))
print("Diccionario combinado:")
print(diccionario_canciones)

# Seleccionar las 3 canciones más largas en un nuevo diccionario
canciones_largas = dict(sorted(diccionario_canciones.items(), key=lambda x: x[1], reverse=True)[:3])
print("\nLas 3 canciones más largas:")
print(canciones_largas)

# Crear un diccionario con una selección aleatoria de canciones
canciones_aleatorias = dict(random.sample(diccionario_canciones.items(), k=2))
print("\nSelección aleatoria de canciones:")
print(canciones_aleatorias)