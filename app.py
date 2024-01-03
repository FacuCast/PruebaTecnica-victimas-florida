import pandas as pd
import zipfile

zip_filename = 'victims.zip'
excel_filename = 'Victims_Age_by_Offense_Category_2022.xlsx'
csv_output_filename = 'output.csv'

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extract(excel_filename)

df = pd.read_excel(excel_filename, skiprows=12, nrows=12, usecols=lambda x: x not in [1], index_col=None)

df.to_csv(csv_output_filename, index=False)
print(df)
print(f'El archivo CSV ha sido guardado como {csv_output_filename}')
