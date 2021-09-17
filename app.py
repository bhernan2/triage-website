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

from index import _content, _title, n_row, _mission, _teams

# _navbar = nav()
# insects=_insect_row()

# content = _content()
title = _title()
nav_row=n_row()
mission_row = _mission()
teams_row =_teams()


def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    # content,
    nav_row,
    title,
    mission_row,
    teams_row
    ])
    return layout

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server
app.layout = Dashboard()



if __name__ == "__main__":
    app.run_server(debug=True)