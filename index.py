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

item1 = [
    dbc.DropdownMenuItem("Misson"),
    dbc.DropdownMenuItem("Goal"),
    
]
item2 = [
    dbc.DropdownMenuItem("Misson"),
    dbc.DropdownMenuItem("Goal"),
    
]


navbar= html.Div([
        dbc.Nav([
            html.Div([
                dbc.DropdownMenu(item1, label="ABOUT US", color="", className="dd-1", bs_size="lg"),
                dbc.DropdownMenu(label="Secondary", color="", className="dd-2", bs_size="lg",),
                dbc.DropdownMenu(label="Success", color="", className="dd-3", bs_size="lg",),
                dbc.DropdownMenu(label="Warning", color="", className="dd-4", bs_size="lg",),
                dbc.DropdownMenu(label="Danger", color="", className="dd-5", bs_size="lg",),
                dbc.DropdownMenu(label="Info", color="", className="dd-6", bs_size="lg",),
                dbc.DropdownMenu(label="Link", color="", className="dd-7", bs_size="lg",),
            ], className='dd-style' )
        ])
    ])

def _content():
    heading = content
    return heading

def ddowns():
    heading = items
    return heading 

def nav():
    heading = navbar
    return heading
