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

home = html.Div([
    dbc.Container([
        dbc.Row([
        dbc.ButtonGroup([
            dbc.Button("HOME", id="tab-1", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}, n_clicks=0),
            dbc.Button("ABOUT", id="tab-2", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.Button("TEAMS",  id="tab-3", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.Button("PROJECTS", id="tab-4", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.Button("PUBLICATIONS", id="tab-5", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.Button("EVENTS", id="tab-6", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
        ],className="buttons", id="buttons"),
    ],className='tab-row'),
    ], className="button-container"),
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
                            ], className='welcome-col'),
                        dbc.Col([
                            dbc.Row([
                                    dbc.CardImg(src="/assets/mayfly.gif")], className='logo'),
                            ],className='welcome-col4'),
                        ], className="welcome-row")
                    ],),
                        dbc.Row([
                            dbc.Col([
                                html.P("We are a cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.",),
                            ], className='welcome-col3')
                          
                        ]),
            
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="home")
mission= html.Div([
    dbc.Container([
       dbc.Row([ 
           dbc.Col([html.P(["Mission"]),
           ]),
        ], className="mission-row"),
        dbc.Row([
            dbc.Col([html.P("Space for a mission statement. What words come to mind when you think of TRIAGE?")
        ],)  
        ], className="mission-content")    
    ], className="mission-contaioner")
], id="mission")

teams = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([ html.P(["Meet the Teams"])
            ],),
        ], className="teams-col"),
        html.Br(),
        dbc.Row([
            dbc.Col([html.P("Space for a carousel component. This component creates a slideshow that cycles through a series of content. The content can highlight collaborators' labs and could include photos and links to lab websites...or whatever...")
        ],)  
        ], className="teams-content")    
    ])
], id="teams")




def _content():
    heading = content
    return heading
def _home():
    heading=home
    return heading 
def _mission():
    heading=mission
    return heading 
def _teams():
    heading=teams
    return heading 

