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

# item1 = [
#     dbc.DropdownMenuItem("Misson"),
#     dbc.DropdownMenuItem("Goal"),
    
# ]
# item2 = [
#     dbc.DropdownMenuItem("Lab 1"),
#     dbc.DropdownMenuItem("Lab 2"),
#     dbc.DropdownMenuItem("Lab 3"),
#     dbc.DropdownMenuItem("....."),

    
#]

nav_row = html.Div([
    dbc.Tabs([
        dbc.Tab(label="HOME", id="tab-1",className="tab"),
        dbc.Tab(label="ABOUT US", id="tab-2"),
        dbc.Tab(label="MEET THE TEAMS",  id="tab-3"),
        dbc.Tab(label="PROJECTS", id="tab-4"),
        # dbc.DropdownMenu(label="PUBLICATIONS", color="", bs_size='lg'),
        dbc.Tab(label="EVENTS", id="tab-5"),
    ],className='dd-row'),
    ],)

# navbar= html.Div([
#         dbc.Nav([
#             html.Div([
#                 dbc.DropdownMenu(item1, label="ABOUT US", color="", className="dd-1", bs_size="lg"),
#                 dbc.DropdownMenu(item2, label="MEET THE TEAMS", color="", className="dd-2", bs_size="lg",),
#                 dbc.DropdownMenu(label="PROJECTS", color="", className="dd-3", bs_size="lg",),
#                 dbc.DropdownMenu(label="PUBLICATIONS", color="", className="dd-4", bs_size="lg",),
#                 dbc.DropdownMenu(label="EVENTS", color="", className="dd-5", bs_size="lg",),
#             ],className='dd-style' )
#         ],)
#     ])

title = html.Div([
    dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Welcome to TRIAGE"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.H4('Texas'),
                            html.H4("Research",), #5/4/21 USACE meeting Research vs River was mentioned
                            html.H4("Institute for",),
                            html.H4("Aquatic &",),
                            html.H4("Groundwater",),
                            html.H4("Ecology",),
                            ], className='welcome-col'),
                        dbc.Col([
                            html.Br(),
                            # dbc.Row([html.H5(""),],className='logo-col'),
                            html.Div([
                            dbc.CardImg(src="/assets/orb.jpg", bottom=True)], className='logo'),
                           
                            ],'welcome-col2'),
                        ])
                    # html.H3(["Texas River Institute for Aquatic & Groundwater Ecology"],className='title-style'),  
                    ],),
                        dbc.Row([
                            dbc.Col([
                                html.Div([
                                html.H5("We are a cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems."),
                            ],className="motto-header")
                            ], className='welcome-col3')
                          
                        ]),
            
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
    dbc.Row([
        html.P(["Mission"])
    ], className='mission-row')
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
def n_row():
    heading=nav_row
    return heading 