import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

from datetime import datetime

from index import nav, ddowns

_navbar = nav()


def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    _navbar, 
    ])
    return layout

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server
app.layout = Dashboard()

if __name__ == "__main__":
    app.run_server(debug=True)