try:
    # Intenta abrir el archivo en modo de lectura ('r')
    with open("mi_archivo.txt", 'r') as file:
        # Si el archivo existe, emite un mensaje de error y no puedes continuar
        print("El archivo ya existe. No puedes continuar.")
except FileNotFoundError:
    # Si el archivo no existe, emite un mensaje y crea un nuevo archivo
    print("El archivo no existe. Creando un nuevo archivo.")
    
    with open("mi_archivo.txt", 'w') as file:
        # Escribe algunas líneas de texto en el archivo
        file.write("Primera línea de texto.\n")
        file.write("Segunda línea de texto.\n")
        file.write("Tercera línea de texto.\n")
        file.write("Cuarta línea de texto.\n")
        file.write("Quinta línea de texto.\n")

# Abre el archivo en modo de lectura
with open("mi_archivo.txt", 'r') as file:
    # Utiliza un bucle con readline para leer y mostrar cada línea del archivo
    line = file.readline()
    while line:
        # Muestra cada línea en la consola
        print(line.strip())
        # Usa tell() para obtener la posición actual del cursor
        print("Posición del cursor:", file.tell())
        # Lee la próxima línea
        line = file.readline()

with open("mi_archivo.txt", 'w') as file:
    file.write("Nueva línea de texto (sobrescribiendo el archivo).\n")

# Abre el archivo en modo de anexar ('a+') y agrega otra línea de texto al final
with open("mi_archivo.txt", 'a+') as file:
    file.write("Otra línea de texto (añadiendo al final).\n")
    # Usa seek(0) para volver al inicio
    file.seek(0)
    # Lee el archivo completo con file.read()
    content = file.read()
    print("Contenido del archivo después de añadir y volver al inicio:")
    print(content)

# Cambia el modificador de 'a+' a 'a' y vuelve a ejecutar el mismo código
# a' no permite operaciones de lectura
with open("mi_archivo.txt", 'a') as file:
    # Esta línea causará un error si se intenta ejecutar aquí
    # content = file.read()
    pass  # No se ejecutará debido a la línea anterior