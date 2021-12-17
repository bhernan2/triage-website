# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

from datetime import datetime

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "black",
    "color":"white",
}

CONTENT_STYLE = {
    "position":"static",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "color": "black",
    
    
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


sidebar = html.Div([
    dbc.Row([
        dbc.Col([html.P("T", style={"color":"black", "background-color":"white", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "text-align":"center", "border":"7px solid #000",}),]),
        dbc.Col([html.H2("TRIAGE", style={"font-size":"25pt", "color":"white", }),], style={"justify-content": "left", "padding-right":"3rem"}),
        ]),

        html.Hr(),
        
        dbc.Nav(
            [
                dbc.NavLink("Home", style={"color":"white", "font-size":"12pt"}, href="#start", external_link=True),
                dbc.NavLink("About", style={"color":"white", "font-size":"12pt"}, href="#mid",external_link=True),
                dbc.NavLink("Teams", style={"color":"white", "font-size":"12pt"}, href="#mid2",external_link=True),
                dbc.NavLink("Projects", style={"color":"white", "font-size":"12pt"}, href="#mid3",external_link=True),
                dbc.NavLink("Publications", style={"color":"white", "font-size":"12pt"}, href="#end",external_link=True),
                html.P('Developed by: Bianca A. Hernandez', style={"font-size": "8pt", "margin-top":"28rem", "text-align":"center"}),
                
                
        ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(
            html.Div([
                dbc.Row(id="start", style={"height":"25rem","background-image":"url('assets/background.jpeg')", "background-position":"center center", "border":"black",}),
                dbc.Row([
                    html.P("Texas Research Institute for Aquatic & Groundwater Ecology", style={"font-weight":"bold", "font-size":"28pt", "padding": "2rem 1rem",}),
                  ], style={"justify-content":"center",}),
                html.Hr(),
                dbc.Row([
                    html.P("A cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",}),
                    ]),
                ] +
                [html.Br()]*50 + 
                [dbc.Row([
                    html.P("Mission & Goals", id="mid", style={"font-weight":"bold", "font-size":"28pt", "padding": "2rem 1rem",}),
                  ], style={"justify-content":"center"}),
                html.Hr(),
                dbc.Row([
                    html.P("The climate crisis is affecting and threatening aquatic ecosystems and the benefits and services these systems provide. Our collaborative research aims to better understand and predict the impacts of climatic changes on aquatic communities. A central focus of research is determining the factors underlying the distribution of aquatic organisms and how increased frequency and intensity of hydrological disturbances will affect the ecology of aquatic ecosystems. The key mission of TRIAGE is to contribute to an increase in diversity (visible and invisible) in aquatic sciences by building and maintaining a diverse and inclusive research team, educating and training students from diverse backgrounds, and promoting broader engagement through outreach to the public.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",})
                    ]),
                ] +           
                [html.Br()]*50 +

                [dbc.Row([
                    html.P("Teams", id="mid2", style={"font-weight":"bold", "font-size":"28pt", "padding": "2rem 1rem",}),
                  ], style={"justify-content":"center"}),
                html.Hr(),
                dbc.Row([
                    dbc.Col([
                                dbc.Card([
                                    dbc.CardImg(src="/assets/fatmucket.svg", style={"color":"black", "width":"180pt", "height":"140"}), 
                                    # dbc.CardBody([
                                    #     html.A("Schwalb: Stream Ecology", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt",})
                            ],),
# color:black;
# align-items: center;
# margin-left: 1.5em;
# width: 180pt;
# height: 140pt;
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/ephemeoptera.svg",style={"color":"black", "width":"180pt", "height":"140pt"}), 
                                    # dbc.CardBody([
                                    #     html.A("Nowlin: Aquatic Ecology", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black"}),
                                    # ]), 
                                ],style={"wwidth":"200pt", "height":"160pt"})
                            ]),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/microbes.svg",style={"color":"black", "width":"180pt", "height":"140pt"}),
                                    # dbc.CardBody([
                                    #     html.A("Another Lab", href="", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt"})
                                
                            ]),
                    ], style={"align-items":"center"}),
                ] +    
                                  [html.Br()]*50 +
                [html.P("Projects", id="mid3")] +
                                  [html.Br()]*50 +
                [html.P("Publications", id="end")]
                                 ),
    id="page-content", style=CONTENT_STYLE)




app = dash.Dash( __name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}], suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE], )
server = app.server
app.layout = html.Div([sidebar, content])


if __name__ == "__main__":
    app.run_server(debug=True)