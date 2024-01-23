import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
 
# Descargar y cargar los datos en un DataFrame
url = "https://drive.google.com/uc?export=download&id=10JJmUmZaDE8k8AQs2gKbPZGPmrIH6GQG"
df = pd.read_csv(url)
 
# Visualizar valores faltantes con matriz de ausencia
plt.figure()
msno.matrix(df)
plt.title("Matriz de Ausencia")
plt.show()
 
# Visualizar valores faltantes con gráfico de barras
plt.figure()
msno.bar(df)
plt.title("Gráfico de Barras de Valores Faltantes")
plt.show()
 
# Visualizar valores faltantes con mapa de calor
plt.figure()
msno.heatmap(df)
plt.title("Mapa de Calor de Valores Faltantes")
plt.show()