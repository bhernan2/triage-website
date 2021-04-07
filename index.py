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
    dbc.DropdownMenuItem("Lab 1"),
    dbc.DropdownMenuItem("Lab 2"),
    dbc.DropdownMenuItem("Lab 3"),
    dbc.DropdownMenuItem("....."),

    
]




navbar= html.Div([
        dbc.Nav([
            html.Div([
                dbc.DropdownMenu(item1, label="ABOUT US", color="", className="dd-1", bs_size="lg"),
                dbc.DropdownMenu(item2, label="MEET THE TEAMS", color="", className="dd-2", bs_size="lg",),
                dbc.DropdownMenu(label="PROJECTS", color="", className="dd-3", bs_size="lg",),
                dbc.DropdownMenu(label="PUBLICATIONS", color="", className="dd-4", bs_size="lg",),
                dbc.DropdownMenu(label="EVENTS", color="", className="dd-5", bs_size="lg",),
                # dbc.DropdownMenu(label="Info", color="", className="dd-6", bs_size="lg",),
                # dbc.DropdownMenu(label="Link", color="", className="dd-7", bs_size="lg",),
            ], className='dd-style' )
        ])
    ])

title = html.Div([
    dbc.Container([
        dbc.Card([
                dbc.CardHeader([
                html.Div([
                    html.P(["Welcome to TRIAGE"],),
                    ],)
                ],className='card-header'),
                dbc.CardBody([
                html.Div([
                    # html.H3(["Texas River Institute for Aquatic & Groundwater Ecology"],className='title-style'),
                    html.H3('Texas'),
                    html.H3("River",),
                    html.H3("Institute for",),
                    html.H3("Aquatic &",),
                    html.H3("Groundwater",),
                    html.H3("Ecology",),
                ],),
                html.Br(),
                html.Br(),
                html.P(
                    "This jumbotron occupies the entire horizontal "
                    "space of its parent.",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "You will need to embed a fluid container in "
                    "the jumbotron.",
                    className="lead",
                ),
            ]),
        ],className='card-style'),
    ],className='title-container', fluid=True,)
], className='img-style')
def _title():
    heading= title
    return heading

def _content():
    heading = content
    return heading

def ddowns():
    heading = items
    return heading 

def nav():
    heading = navbar
    return heading
