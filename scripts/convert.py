import pandas as pd 

#Converteert de excelsheet naar een CSV voor makkelijke data vergelijkingen
df = pd.read_excel('supdata1.xlsx' , sheet_name = 'Pop. F Sequencing Statistics')  # sheetname is optional
df.to_csv('supdata_f_sequencing.csv', index=False)  # index=False prevents pandas to write row index