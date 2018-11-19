import pandas as pd 
import matplotlib.pyplot as plt 

# Leest de data van de .csv file
path_to_file = "../supdata/supdata_f_metadata.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')

# Print de data van de diagnosis van de datagroep
# print(data.Diagnosis)
a = data.Diagnosis.value_counts(sort='true')




# Maakt een grafiek van de diagnosis
plt.bar(a, height='20')

plt.ylabel('Aantal')
plt.show()
