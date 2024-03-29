# -*- coding: utf-8 -*-

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

content = html.Div([
    # html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
        # dbc.ButtonGroup([
        #     dbc.Button("HOME", id="tab-1", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"},),
        #     dbc.Button("ABOUT", id="tab-2", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
        #     dbc.Button("TEAMS",  id="tab-3", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
        #     dbc.Button("PROJECTS", id="tab-4", style={"color": "black", "border-style":"none", "margin":"10px","font-size": 20, "background":"white","cursor":"pointer"}),
        #     dbc.Button("PUBLICATIONS", id="tab-5", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
        #     dbc.Button("EVENTS", id="tab-6", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
        # ],className="buttons", id="tabs"),
    ],className='tab-row', justified=True),
    ], className="button-container"),
   dbc.Container([
       dbc.Row([
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
                            dbc.CardImg(src="/assets/mayfly.gif",className="mayfly-col" )
                        ]),
                        dbc.Col([
                            dbc.Row([html.P('T',style={"color": "black", "font-size": 40, "font-weight":"bolder", "margin-top": "0rem"}),html.P('exas', style={"color": "black", "font-size": 20, "font-weight":"normal", "margin-top": "1.1rem",} ),]),
                            dbc.Row([html.P('R',style={"color": "black", "font-size": 40, "font-weight":"bolder","margin-top": "0rem"}),html.P('esearch', style={"color": "black", "font-size": 20, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('I',style={"color": "black", "font-size": 40, "font-weight":"bolder","margin-top": "0rem"}),html.P('nstitute for', style={"color": "black", "font-size": 20, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('A',style={"color": "black", "font-size": 40, "font-weight":"bolder","margin-top": "0rem"}),html.P('quatic &', style={"color": "black", "font-size": 20, "font-weight":"normal","margin-top": "1.1rem"} ),]),
                            dbc.Row([html.P('G',style={"color": "black", "font-size": 40, "font-weight":"bolder","margin-top": "0rem"}),html.P('roundwater', style={"color": "black", "font-size": 20, "font-weight":"normal","margin-top": "1rem"} ),]),
                            dbc.Row([html.P('E',style={"color": "black", "font-size": 40, "font-weight":"bolder","margin-top": "0rem"}),html.P('cology', style={"color": "black", "font-size": 20, "font-weight":"normal","margin-top": "1.2rem"} ),]),
                            ], className='triage-col'),
                        ],className="welcome-box")
                    ]),
                        dbc.Col([
                            html.P("We are a cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.",),
                                
                            ], className='welcome-col3')
            
            ], className="teams-content"),
        ],className='card-style'),
       ])
    ], className='card-container',),
    
], id="page-content", className='content-style')

# home = html.Div([
    
# ], id="home")
mission= html.Div([
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
    ], className="button-container"),
   dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Mission"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space for a mission statement. What words come to mind when you think of TRIAGE?"),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br()
                            
                        ]),
                        ],className="teams-content")  
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="page-content", className='content-style')

teams=html.Div([
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
    ], className="button-container"),
   dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Teams"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space for a carousel component. This component creates a slideshow that cycles through a series of content. The content can highlight collaborators' labs and could include photos and links to lab websites...or whatever..."),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br()
                        ]),
                        ],className="teams-content")  
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="page-content", className='content-style')

projects= html.Div([
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
    ], className="button-container"),
   dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Projects"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight projects..."),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br()
                        ]),
                        ],className="teams-content")  
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="page-content", className='content-style')

publications=html.Div([
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
    ], className="button-container"),
   dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Publications"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight publications..."),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br()
                        ]),
                        ],className="teams-content")  
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="page-content", className='content-style')

events=html.Div([
    html.Br(),
    dbc.Container([
        dbc.Row([
            dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
            dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
    ],className='tab-row'),
    ], className="button-container"),
   dbc.Container([
        dbc.Card([
                dbc.Row([
                html.Div([
                    html.P(["Events"],),
                    ],className='card-header')
                ],),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight events..."),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br(),
                            html.Br()
                        ]),
                        ],className="teams-content")  
            ]),
        ],className='card-style'),
    ], className='card-container', fluid=True,),
], id="page-content", className='content-style')
footer = dbc.Row([
        dbc.Col([
            html.P("Created by: Bianca A. Hernandez"),
        ], className="signature"),
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon")

        ], className="social-col")
    ], className="footer-row")

def _content():
    heading=content
    return heading
def _mission():
    heading=mission
    return heading 
def _teams():
    heading=teams
    return heading
def _projects():
    heading=projects
    return heading 
def _publications():
    heading=publications
    return heading
def _events():
    heading = events
    return heading 
def _footer():
    heading=footer
    return heading


# def Dashboard():
#     layout= html.Div([
#     dcc.Location(id="url"), 
#     content, 
#     footer
#     ])
#     return layout

# app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE])
# server = app.server
# app.layout = Dashboard()

# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return content
#     elif pathname == "/page-1":
#         return mission
#     elif pathname == "/page-2":
#         return teams
#     elif pathname == "/page-3":
#         return projects
#     elif pathname == "/page-4":
#         return publications
#     elif pathname == "/page-5":
#         return events

# if __name__ == "__main__":
#     app.run_server(debug=True)