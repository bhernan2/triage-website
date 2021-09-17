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

nav_row = html.Div([
    dbc.Tabs([
        dbc.Tab(label="HOME", id="tab-1", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"whitesmoke","cursor":"pointer"}),
        dbc.Tab(label="ABOUT US", id="tab-2", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"whitesmoke","cursor":"pointer"}),
        dbc.Tab(label="MEET THE TEAMS",  id="tab-3", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"whitesmoke","cursor":"pointer"}),
        dbc.Tab(label="PROJECTS", id="tab-4", label_style={"color": "black", "font-size": 22, "margin-top": "2rem", "background":"whitesmoke","cursor":"pointer"}),
        # dbc.DropdownMenu(label="PUBLICATIONS", color="", bs_size='lg'),
        dbc.Tab(label="EVENTS", id="tab-5", label_style={"color": "black", "font-size": 22,"margin-top": "2rem", "background":"whitesmoke","cursor":"pointer"}),
    ],className='tab-row', id="card-tabs", card=False, active_tab="tab-1"),
    ],)

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
                            dbc.Row([
                                    dbc.CardImg(src="/assets/mayfly.gif")], className='logo'),
                        ],className='welcome-col2'),
                        dbc.Col([
                            dbc.Row([html.P('T',style={"color": "black", "font-size": 50, "font-weight":"bolder", "margin-top": "0rem"}),html.P('exas', style={"color": "black", "font-size": 30, "font-weight":"normal", "margin-top": "1.1rem",} ),]),
                            dbc.Row([html.P('R',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem"}),html.P('esearch', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('I',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem"}),html.P('nstitute for', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('A',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem"}),html.P('quatic &', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('G',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem"}),html.P('roundwater', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem"} ),]),
                            dbc.Row([html.P('E',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem"}),html.P('cology', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1.2rem"} ),]),
                            # html.P("Research",style={"color": "black", "font-size": 30,}), #5/4/21 USACE meeting Research vs River was mentioned
                            # html.P("Institute for",style={"color": "black", "font-size": 30,}),
                            # html.P("Aquatic &",style={"color": "black", "font-size": 30,}),
                            # html.P("Groundwater",style={"color": "black", "font-size": 30,}),
                            # html.P("Ecology",style={"color": "black", "font-size": 30, "margin-bottom": "2rem",}),
                            ], className='welcome-col'),
                        dbc.Col([
                            # dbc.Row([html.H5(""),],className='logo-col'),
                            dbc.Row([
                                    dbc.CardImg(src="/assets/mayfly.gif")], className='logo'),
                            ],className='welcome-col4'),
                        ], className="welcome-row")
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
], className='img-style')

mission= html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([ html.P(["Mission"], className="mission-title")
            ],),
        ], className="mission-col"),
        dbc.Row([
            dbc.Col([html.P("Space for a mission statement. What words come to mind when you think of TRIAGE?")
        ],)  
        ], className="mission-content")    
    ])
])

teams = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([ html.P(["Meet the Teams"], className="mission-title")
            ],),
        ], className="teams-col"),
        dbc.Row([
            dbc.Col([html.P("Space for a carousel component. This component creates a slideshow that cycles through a series of content. The content can highlight collaborators' labs and could include photos and links to personal websites...or whatever...")
        ],)  
        ], className="teams-content")    
    ])
])



def _title():
    heading= title
    return heading
def _content():
    heading = content
    return heading
def n_row():
    heading=nav_row
    return heading 
def _mission():
    heading=mission
    return heading 
def _teams():
    heading=teams
    return heading 

