import pandas as pd
import zipfile

# Nombre del archivo zip y del archivo Excel dentro del zip
zip_filename = 'victims.zip'
excel_filename = 'Victims_Age_by_Offense_Category_2022.xlsx'
csv_output_filename = 'output.csv'

# Leer el archivo zip
with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    # Extraer el archivo Excel
    zip_ref.extract(excel_filename)

# Leer el archivo Excel con pandas y omitir la columna 2
df = pd.read_excel(excel_filename, skiprows=12, nrows=12, usecols=lambda x: x not in [1], index_col=None)

# Mostrar el DataFrame resultante


# Guardar el DataFrame en un archivo CSV
df.to_csv(csv_output_filename, index=False)
print(df)
# Imprimir un mensaje de confirmación
print(f'El archivo CSV ha sido guardado como {csv_output_filename}')
