#!/usr/bin/env python
# coding: utf-8

# Deploying Dash App using Render: An Example
import os
import numpy as np
import pandas as pd
from dash import Dash, dcc, html, Output, Input
import plotly.express as px

# Load dataset
df = px.data.tips()

# Initialize Dash app
app = Dash(__name__)
server = app.server  # required for Render deployment

# Define layout
radio_b = dcc.RadioItems(df.columns, 'time')
my_graph = dcc.Graph()
app.layout = html.Div([radio_b, my_graph])

# Define callback
@app.callback(Output(my_graph, 'figure'), Input(radio_b, 'value'))
def update_graph(value):
    fig = px.bar(df, x=value, y="tip")
    return fig

# Run app on Render-compatible host and port
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
