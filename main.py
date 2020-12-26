#!/usr/bin/env python

import plotly.graph_objects as go
import plotly.express as px
import numpy as np

xData = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
yData = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

fig = go.Figure()

fig.add_trace(go.Scatter(x=xData, y=yData))

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)