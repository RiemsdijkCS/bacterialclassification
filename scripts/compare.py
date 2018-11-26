import pandas as pd
import matplotlib.pyplot as plt

# Leest de data van de .csv file
path_to_file = "../supdata/supdata_f_metadata.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')

#sort de data zodat de N/A waarden worden gedropt (Houdt alleen cancer over.)
sorted_data = data.dropna()

mean_age = sorted_data.Age.mean()
print(mean_age)
mean_BMI = sorted_data.BMI.mean()
print(mean_BMI)
mean_TNM = sorted_data.TNM.value_counts()
print(mean_TNM)





# a = data.groupby('Diagnosis').Age.mean()
# b = data[data.Diagnosis == ['Cancer']]
# c = data.groupby('Diagnosis')
# d = data.dtypes