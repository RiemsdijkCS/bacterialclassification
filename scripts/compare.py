import pandas as pd
import matplotlib.pyplot as plt

# Leest de data van de .csv file
path_to_file = "../supdata/supdata_f_metadata.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')

# a = data.groupby('Diagnosis').Age.mean()
# b = data[data.Diagnosis == ['Cancer']
# c = data.groupby('Diagnosis')


# print(a)
# print(b)
# print(c)
