import pandas as pd
#Import de dataframes benodigd voor het mergen van de 2 DF.
dataframe_metadata = pd.read_csv('supdata_f_metadata.csv')
dataframe_toxic = pd.read_csv('taxonomic.csv')
#Maak een list van de dataframes.
frames = [dataframe_metadata, dataframe_toxic]
#Concatenate de DFs samen maar over axis=1 dus niet naar beneden maar rechts. 
result = pd.concat(frames,axis=1, ignore_index=False, sort=False)
#Convert het result naar een csv file.
result.to_csv('merged.csv')
