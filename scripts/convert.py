import pandas as pd 

#Converteert de excelsheet naar een CSV voor makkelijke data vergelijkingen
df = pd.read_excel('../supdata/supdata3.xlsx', sheetname="Taxonomic")  # sheetname is optional
df.to_csv('taxonomic.csv', index=False)  # index=False prevents pandas to write row index