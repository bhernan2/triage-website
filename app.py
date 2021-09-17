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

from index import _content, _home, _mission, _teams


# _navbar = nav()
# insects=_insect_row()

# content = _content()
# title = _title()
home_row=_home()
mission_row = _mission()
teams_row =_teams()



def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    # content,
    home_row,
    # title,
    mission_row,
    teams_row, 
    ])
    return layout

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server
app.layout = Dashboard()

# @app.callback(
#     Output("home", "children"), [Input("buttons", "n_clicks")]
# )
# def on_button_click(n):
#     if n is None:
#         return home_row
#     elif n == "tab-1":
#         return home_row
#     elif n == "tab-2":
#         return mission_row 

if __name__ == "__main__":
    app.run_server(debug=True)