from typing import Container
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

# insect_row=html.Div([
#     dbc.Container([
#         dbc.Row([
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ])
#         ], className="insect-1"),
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ]),
#         ], className="insect-2"),
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ]),
#         ], className="insect-3"),
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ]),
#         ], className="insect-4"),
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ]),
#         ], className="insect-5"),
#         dbc.Card([
#         dbc.CardBody([
#             dbc.CardImg(src="/assets/mayfly.gif")
#         ]),
#         ], className="insect-6"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-7"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-8"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-9"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-10"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-11"),
#         # dbc.Card([
#         # dbc.CardBody([
#         #     dbc.CardImg(src="/assets/mayfly.gif")
#         # ]),
#         # ], className="insect-12"),
#     ],className="insects-row")
#     ],className="insects-containter"),   
# ])
nav_row = html.Div([
    dbc.Tabs([
        dbc.Tab(label="HOME", id="tab-1", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"white","cursor":"pointer"}),
        dbc.Tab(label="ABOUT US", id="tab-2", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"white","cursor":"pointer"}),
        dbc.Tab(label="MEET THE TEAMS",  id="tab-3", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"white","cursor":"pointer"}),
        dbc.Tab(label="PROJECTS", id="tab-4", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"white","cursor":"pointer"}),
        # dbc.DropdownMenu(label="PUBLICATIONS", color="", bs_size='lg'),
        dbc.Tab(label="EVENTS", id="tab-5", label_style={"color": "black", "font-size": 22,"margin-top": "2rem", "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
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
                                html.P("We are a cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.",),
                            ], className='welcome-col3')
                          
                        ]),
            
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
    dbc.Row([
        html.P(["Mission"])
    ], className='mission-row'),
], className='img-style')

# carousel=dbc.Row([
#         html.P(["Meet the Teams"]),
#         dbc.(
#             items=[
#                 {"key": "1", "src": "/assets/orb.jpg"},
#                 {"key": "2", "src": "/assets/orb.jpg"},
#                 {"key": "3", "src": "/assets/orb.jpg"},
#             ],
#     controls=True,
#     indicators=True,
#         ),
#     ])
def _title():
    heading= title
    return heading

def _content():
    heading = content
    return heading

def ddowns():
    heading = items
    return heading 
# def _insect_row():
#     heading = insect_row
#     return heading 

# def nav():
#     heading = nav_row
#     return heading
def n_row():
    heading=nav_row
    return heading 