import plotly.express as px  
import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly  


 
#open the file
vote=pd.read_csv('sales.csv')
print(vote.columns)
df=DataFrame(vote)



continent=df['Place']
country=df['Country']
region=df['City']
sales=df['Out_px']
margin=df['Margin']
remark=df['Products']

#create the treemap

fig=px.treemap(df,
path=[continent, region, country],
values=sales,
color=margin,
color_continuous_scale=['red','green','green'],
title='Sales_overview',
hover_name=remark     
)

#setting a layout(optional task)

fig.update_layout(
    title_font_size=42,
    title_font_family='Arial'
)

#save html to easily access the chart 

plotly.offline.plot(fig, filename='Sales_chart')






