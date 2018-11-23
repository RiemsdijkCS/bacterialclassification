import pandas as pd 
import matplotlib.pyplot as plt 

# Leest de data van de .csv file
path_to_file = "../supdata/supdata_f_metadata.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')

#Set de x en y waarden
x = ['Normal', 'Small Adenoma', 'Large Adenoma', 'Cancer' ]
y = data.Diagnosis.value_counts(sort='true')


# Maakt een grafiek van de diagnosis
plt.bar(x,height=y, width=0.8, )
plt.xlabel('Diagnosis')
plt.ylabel('Aantal')
plt.title('Diagnosis datagroep F')
plt.show()
