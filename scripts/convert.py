import pandas as pd 

#Converteert de excelsheet naar een CSV voor makkelijke data vergelijkingen
df = pd.read_excel('../model_2.xlsx')  # sheetname is optional
df.to_csv('model_2.csv', index=False)  # index=False prevents pandas to write row index