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

content = html.Div(html.Br(), id="page-content", className='content-style')

items = [
    dbc.DropdownMenuItem("Item 1"),
    dbc.DropdownMenuItem("Item 2"),
    dbc.DropdownMenuItem("Item 3"),
]

navbar= html.Div([
        dbc.Nav([
            html.Div([
                dbc.DropdownMenu(items, label="Primary", color="primary", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Secondary", color="secondary", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Success", color="success", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Warning", color="warning", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Danger", color="danger", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Info", color="info", className="m-1", bs_size="lg",),
                dbc.DropdownMenu(items, label="Link", color="link", className="m-1", bs_size="lg",),
            ],className='dd-style', style=dict(display='flex'))
        ], )
    ], className='navbar-style',)

def _content():
    heading = content
    return heading

def ddowns():
    heading = items
    return heading 

def nav():
    heading = navbar
    return heading
