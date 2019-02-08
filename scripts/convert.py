import pandas as pd 

#Converteert de excelsheet naar een CSV voor makkelijke data vergelijkingen
df = pd.read_excel('../final/model.xlsx')  # sheetname is optional
df.to_csv('model.csv', index=False)  # index=False prevents pandas to write row index