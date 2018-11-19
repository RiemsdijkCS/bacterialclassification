import plotly.plotly as py 
import plotly.graph_objs as go
import plotly
plotly.tools.set_credentials_file(username='ChrisRiemsdijk', api_key='wzanDIvWjT3ZyJkxqz52')

# Heb plotly geprobeerd maar de pandas module is toch fijner 
import pandas as pd

df = pd.read_csv('supdata/supdata_f_metadata.csv')

trace = go.Table(
    header=dict(values=list(df.columns),
                fill=dict(color='#C2D4FF'),
                align=['left'] * 5),

    cells=dict(values=[df.SubjectID, df.SampleID, df.Age],
    fill = dict(color='#F5F8FF'),
    align = ['left'] *5)
)

data = [trace]
py.plot(data, filename = 'pandastable')