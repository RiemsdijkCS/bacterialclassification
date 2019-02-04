import pandas as pd
from scipy import stats

df = pd.read_csv('merged.csv')


# a = stats.ttest_ind(df.Methanoculleus_marisnigri[df.Diagnosis == 'Cancer'][df.Diagnosis == "Small Adenoma"],df.Methanoculleus_marisnigri[df.Diagnosis == 'Normal'])

for column in df:
    p = stats.ttest_ind(df.loc[df['Diagnosis'] =='Cancer' | df['Diagnosis'] == 'Small adenoma', column], df.loc[df['Diagnosis'] == 'Normal',column])
    print('kolom', column, ': p=', p)









