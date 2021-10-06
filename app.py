# -*- coding: utf-8 -*-

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
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Welcome to TRIAGE"],),
                    ],className='card-header'),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Row([html.P('T',style={"color": "black", "font-size": 50, "font-weight":"bolder", "margin-top": "0rem","margin-left":"5rem"}),html.P('exas', style={"color": "black", "font-size": 30, "font-weight":"normal", "margin-top": "1rem","text-align":"right"} ),]),
                            dbc.Row([html.P('R',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem","margin-left":"5rem"}),html.P('esearch', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem","text-align":"right"} ),]),
                            dbc.Row([html.P('I',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem","margin-left":"5rem" }),html.P('nstitute for', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem", "text-align":"right"} ),]),
                            dbc.Row([html.P('A',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem","margin-left":"5rem" }),html.P('quatic &', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem", "text-align":"right"} ),]),
                            dbc.Row([html.P('G',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem","margin-left":"5rem" }),html.P('roundwater', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem", "text-align":"right"} ),]),
                            dbc.Row([html.P('E',style={"color": "black", "font-size": 50, "font-weight":"bolder","margin-top": "0rem","margin-left":"5rem" }),html.P('cology', style={"color": "black", "font-size": 30, "font-weight":"normal","margin-top": "1rem", "text-align":"right"} ),]),
                            
                            ],className='triage-col'),
                        dbc.Col([
                            html.P("T", style={"color":"white", "background-color":"black", "font-size":"200px", "border-radius":"100%", "padding":"0rem", "width":"280px", "height":"280px", "border":"10px solid #000","text-align":"center"})
                        ],className="mayfly-col"),
                        dbc.Col([
                                html.P("We are a cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.",),
                            ],className='welcome-col3'),
                        ],className="welcome-box"),
            ]),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col")
    ], className="footer-row")
], id="page-content", className='content-style')

# home = html.Div([
    
# ], id="home")
mission= html.Div([
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Mission & Goals"],),
                    ],className='card-header'),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("The climate crisis is affecting and threatening aquatic ecosystems and the benefits and services these systems provide. Our collaborative research aims to better understand and predict the impacts of climatic changes on aquatic communities. A central focus of research is determining the factors underlying the distribution of aquatic organisms and how increased frequency and intensity of hydrological disturbances will affect the ecology of aquatic ecosystems. The key mission of TRIAGE is to contribute to an increase in diversity (visible and invisible) in aquatic sciences by building and maintaining a diverse and inclusive research team, educating and training students from diverse backgrounds, and promoting broader engagement through outreach to the public.")
                        ])
                        ],className="mission-content"),
            ]),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col"),
    ], className="footer-row"),
], id="page-content", className='content-style')
# carousel = dbc.Carousel(
#     items=[
#         {"key": "1", "src":""},
#         {"key": "2", "src":""},
#         {"key": "3", "src":""},
#     ],
#     controls=True,
#     indicators=True,
# )
teams=html.Div([
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Meet the Teams"],),
                    ],className='card-header'),
                dbc.CardBody([
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/fatmucket.svg", className = 'align-self-center', style={"width":"110pt","height":"90pt",}), 
                                    dbc.CardBody([
                                        html.A("Schwalb Stream Ecology Lab", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"})
                            ]),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/ephemeoptera.svg", className = 'align-self-center', style={"width":"110pt","height":"90pt",}), 
                                    dbc.CardBody([
                                        html.A("Nowlin Aquatic Ecology Lab", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"})
                            ]),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/microbes.svg", className = 'align-self-center', style={"width":"110pt","height":"90pt",}),
                                    dbc.CardBody([
                                        html.A("Another Lab", href="", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"})
                                
                            ]),
                            ],className="teams-cards",),
                        dbc.Row([
                            dbc.Col([
                               dbc.Card([
                                   dbc.CardImg(src="/assets/longnose_dace.svg", className = 'align-self-center', style={"width":"110pt","height":"90pt",}), 
                                    dbc.CardBody([
                                        html.A("Another Lab", href="", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"}) 
                            ]),
                            dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/blind_salamander.svg", className = 'align-self-center', style={"width":"110pt","height":"90pt",}),  
                                    dbc.CardBody([
                                        html.A("Another Lab", href="", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"})
                            ]),
                            dbc.Col([
                                dbc.Card([
                                    # dbc.CardImg(src="/assets/orb.jpg", style={"width":"110pt","height":"90pt", "justify-content":"center"}), 
                                    dbc.CardBody([
                                        html.A("Another Lab", href="", style={"color":"black"}),
                                    ]), 
                                ],style={"width":"220pt", "height":"180pt"})
                            ]),
                            ],className="teams-cards",),
                    ], className="teams-div")
            ], className="cards-styles"),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col")
    ], className="footer-row")
], id="page-content", className='content-style')

projects= html.Div([
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Projects"],),
                    ],className='card-header'),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight projects...")
                        ])
                        ],className="projects-content"),
            ]),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col")
    ], className="footer-row")
], id="page-content", className='content-style')
publications=html.Div([
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Publications"],),
                    ],className='card-header'),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight publications...")
                        ])
                        ],className="publications-content"),
            ]),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col")
    ], className="footer-row")
], id="page-content", className='content-style')

events=html.Div([
    dbc.Container([
            dbc.Row([
                dbc.Col([html.P("T", style={"color":"white", "background-color":"black", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000", "margin-left":"25px"}),], className="small-logo"),
            html.Ul([
                html.Li([
                dbc.NavLink("HOME", href="/", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", }),
                dbc.NavLink("ABOUT", href="/page-1", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("TEAMS", href="/page-2", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PROJECTS", href="/page-3", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("PUBLICATIONS", href="/page-4", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer"}),
                dbc.NavLink("EVENTS", href="/page-5", active="exact", style={"color": "black", "border-style":"none", "margin":"10px", "font-size": 20, "background":"white","cursor":"pointer", "text-align":"right"}),
            ], className="nav-li"),  
            ], className="nav-ul"),
        ],className='tab-row'),
    ], fluid=True, className="link-container"),
   dbc.Container([
       dbc.Row([
           dbc.CardHeader([
                html.Div([
                    html.P(["Events"],),
                    ],className='card-header'),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.P("Space to highlight events...")
                        ])
                        ],className="events-content"),
            ]),
        ],className='card-style'),
       ],className="triage-row"),
    ], className='card-container', fluid=True),
    dbc.Row([
        dbc.Col([
            html.P("© 2021 TRIAGE")
        ],className="copyright-col"),
        dbc.Col([
            html.P("Follow us on:"),
        ], className="follow-us"),
        dbc.Col([
            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
            children=[
                html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",className="facebook-icon")]
            ),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",className="instagram-icon"),
            html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),

        ], className="social-col")
    ], className="footer-row")
], id="page-content", className='content-style')

# def _content():
#     heading=content
#     return heading
# def _mission():
#     heading=mission
#     return heading 
# def _teams():
#     heading=teams
#     return heading
# def _projects():
#     heading=projects
#     return heading 
# def _publications():
#     heading=publications
#     return heading
# def _events():
#     heading = events
#     return heading 


def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    content, 
    ])
    return layout

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE])
server = app.server
app.layout = Dashboard()

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return content
    elif pathname == "/page-1":
        return mission
    elif pathname == "/page-2":
        return teams
    elif pathname == "/page-3":
        return projects
    elif pathname == "/page-4":
        return publications
    elif pathname == "/page-5":
        return events

if __name__ == "__main__":
    app.run_server(debug=True)