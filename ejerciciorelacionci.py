import pandas as pd
import missingno as msno
gasto_educacion = pd.read_csv('https://drive.google.com/uc?export=download&id=10a4935pfdhK8jwkHQf5rM3hWp137G5cT')
print(gasto_educacion.columns)
# Merge externo
merged_df = pd.merge(df1, gasto_educacion, left_on='Country', right_on='Economy', how='outer', indicator=True)
# Identificar no correspondencias
sin_equivalencia_df1 = merged_df[merged_df['_merge'] == 'left_only']
# Crear tabla de equivalencias
tabla_equivalencias = merged_df[['Country', 'Economy']]
tabla_equivalencias['Equivalencia'] = merged_df['_merge'].apply(lambda x: 'Sí' if x == 'both' else 'No')
# Mostrar resultados
print("Elementos sin equivalencia en df1:")
print(sin_equivalencia_df1[['Country']])
print("\nTabla de Equivalencias:")
print(tabla_equivalencias)
df2 = pd.merge(df1, gasto_educacion, left_on='Country', right_on='Economy', how='inner', indicator=True)
df2.to_excel("merged_with_expense_on_education.xlsx", index=False)