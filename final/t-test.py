import pandas as pd
from scipy import stats

df = pd.read_csv('merged.csv')


# a = stats.ttest_ind(df.Methanoculleus_marisnigri[df.Diagnosis == 'Cancer'][df.Diagnosis == "Small Adenoma"],df.Methanoculleus_marisnigri[df.Diagnosis == 'Normal'])

for column in df:
    try:
        p = stats.ttest_ind(df.loc[df['Diagnosis'] == 'Normal',column],df.loc[(df['Diagnosis'] == 'Cancer') | (df['Diagnosis'] == 'Small Adenoma'), column])

        if p.pvalue <= 0.01:
            print("Kolom: ", column, "p= ", p.pvalue)
        else:
            pass

    except:
        pass










