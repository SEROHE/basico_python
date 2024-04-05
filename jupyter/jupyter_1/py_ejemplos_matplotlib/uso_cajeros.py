
import pandas as pd
import matplotlib.pyplot as plt

# Lee el archivo CSV
df = pd.read_csv('943.csv')

# Elimina la columna 'AÑO'
df = df.drop('AÑO', axis=1)

# Agrupa por 'INSTALACION' y 'SERVICIO' y suma los usos
tabla = df.groupby(['INSTALACION', 'SERVICIO'])['USOS'].sum().unstack()

# Configura el gráfico
plt.figure(figsize=(12, 8))

# Itera sobre las columnas de la tabla (los servicios)
for servicio in tabla.columns:
    plt.bar(tabla.index, tabla[servicio], label=servicio)

# Configura etiquetas y leyenda
plt.xlabel('Instalación')
plt.ylabel('Cantidad de usos')
plt.title('Cantidad de usos por instalación para cada servicio')
plt.xticks(rotation=90)
plt.legend(title='Servicio', bbox_to_anchor=(1.05, 1), loc='upper left')

# Muestra el gráfico
plt.tight_layout()
plt.show()