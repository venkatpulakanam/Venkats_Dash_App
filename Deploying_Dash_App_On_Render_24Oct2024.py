#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Deploying Dash App using Render: An Example
# Source: https://docs.google.com/document/d/15P9TIIxKHujkesBnYL_4nLU3Pr9AEKw12Ov-X1Bca7s/edit?tab=t.0
import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
#
df = px.data.tips()
app = Dash(__name__)
server = app.server # added this to use the app via Render
#
radio_b = dcc.RadioItems(df.columns, 'time')
my_graph = dcc.Graph()
app.layout = html.Div([radio_b, my_graph])

@app.callback(Output(my_graph, 'figure'),
              Input(radio_b, 'value'))
def update_graph(value):
   fig = px.bar(df, x=value, y="tip")
   return fig
if __name__ == '__main__':
  app.run()
# if __name__ == '__main__':
  #  app.run_server(debug=False)


# In[ ]:




