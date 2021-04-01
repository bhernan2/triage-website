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

items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
]

navbar= html.Div([
        dbc.Nav([
            html.Div([
                dbc.DropdownMenu(items, label="Primary", color="primary", className="m-1"),
                dbc.DropdownMenu(items, label="Secondary", color="secondary", className="m-1"),
                dbc.DropdownMenu(items, label="Success", color="success", className="m-1"),
                dbc.DropdownMenu(items, label="Warning", color="warning", className="m-1"),
                dbc.DropdownMenu(items, label="Danger", color="danger", className="m-1"),
                dbc.DropdownMenu(items, label="Info", color="info", className="m-1"),
                dbc.DropdownMenu(items, label="Link", color="link", className="m-1"),
            ],style={"display": "flex", "flexWrap": "wrap"},)
        ])
    ])

def ddowns():
    heading = items
    return heading 

def nav():
    heading = navbar
    return heading
