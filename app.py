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

# MOVED TO CUSTOMS.CSS
# the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "black",
#     "color":"white",
#     #this fucking sucks
# }


CONTENT_STYLE = {
    "position":"static",
    "margin-left": "13rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
    "color": "black",
    
    
}

IMG_STYLE = {
    "color":"black", 
    "width":"180pt", 
    "height":"140", 
    "margin-left":"0.5rem", "margin-top":"1rem"

}

# the styles for the main content position it to the right of the sidebar and
# add some padding.


sidebar = html.Div([
    dbc.Row([
        dbc.Col([],),
         ]),
    dbc.Row([
            dbc.Col([html.H2("TRIAGE", style={"font-size":"25pt", "color":"white","padding":"1rem" }),], style={"justify-content": "center",}),
    ]),     
       

        html.Hr(),
        
        dbc.Nav(
            [
                dbc.NavLink("Home", style={"color":"white", "font-size":"12pt"}, href="#start", external_link=True, className="links"),
                dbc.NavLink("About", style={"color":"white", "font-size":"12pt"}, href="#mid",external_link=True),
                dbc.NavLink("Teams", style={"color":"white", "font-size":"12pt"}, href="#mid2",external_link=True),
                dbc.NavLink("Projects", style={"color":"white", "font-size":"12pt"}, href="#mid3",external_link=True),
                dbc.NavLink("Publications", style={"color":"white", "font-size":"12pt"}, href="#end",external_link=True),
                # html.P('Developed by: Bianca A. Hernandez', style={"font-size": "8pt", "margin-top":"28rem", "text-align":"center"}),
                html.P("T", style={"color":"black", "background-color":"white", "font-size":"22px", "font-weight":"bolder", "border-radius":"100%", "width":"44px", "height":"44px", "margin-top":"25.5rem", "margin-left":"3rem", "text-align":"center", "border":"7px solid #000",})
                
        ],
            vertical=True,
            pills=True,
        ),
    ],
    className="SIDEBAR_STYLE"
)

content = html.Div(
            html.Div([
                dbc.Row(id="start", style={"height":"25rem","background-image":"url('assets/background.jpeg')", "background-position":"center center", "border":"black",}),
                dbc.Row([
                    html.P("Texas Research Institute for Aquatic & Groundwater Ecology", style={"font-weight":"bold", "font-size":"28pt", "padding": "1rem",}),
                  ], style={"justify-content":"center",}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("A cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",}),
                    ]),
                ] +
                [html.Br()]*50 + 
                [dbc.Row([
                    html.P("Mission & Goals", id="mid", style={"font-weight":"bold", "font-size":"28pt", "padding": "1rem",}),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("The climate crisis is affecting and threatening aquatic ecosystems and the benefits and services these systems provide. Our collaborative research aims to better understand and predict the impacts of climatic changes on aquatic communities. A central focus of research is determining the factors underlying the distribution of aquatic organisms and how increased frequency and intensity of hydrological disturbances will affect the ecology of aquatic ecosystems. The key mission of TRIAGE is to contribute to an increase in diversity (visible and invisible) in aquatic sciences by building and maintaining a diverse and inclusive research team, educating and training students from diverse backgrounds, and promoting broader engagement through outreach to the public.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",})
                    ]),
                ] +           
                [html.Br()]*50 +

                [dbc.Row([
                    html.P("Teams", id="mid2", style={"font-weight":"bold", "font-size":"28pt", "padding": "1rem",}),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="/assets/fatmucket.svg", style=IMG_STYLE), 
                                ],style={"width":"200pt", "height":"160pt",}),
                            dbc.Row([
                                        html.A("Schwalb: Stream Ecology", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black", "font-size":"18pt", "margin-left":"1rem"}), 
                            ]),
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/ephemeoptera.svg",style=IMG_STYLE), 
                                ],style={"width":"200pt", "height":"160pt", "vertical-align":"middle"}),
                                dbc.Row([
                                        html.A("Nowlin: Aquatic Ecology", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black", "font-size":"18pt", "margin-left":"1.5rem"}), 
                            ]),
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/microbes.svg",style={"color":"black", "width":"180pt", "height":"140",  "margin-left":"1rem", "margin-top":"1rem"}),
                                    # dbc.CardBody([
                                    #     html.A("Another Lab", href="", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt", "vertical-align":"middle"})
                                
                            ],className="card-cols"),
                    ], style={"padding-top":"1rem", "padding-left":"5rem"}),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="/assets/longnose_dace.svg", style={"color":"black", "width":"180pt", "height":"140",  "margin-left":"1rem", "margin-top":"3.5rem"}), 
                                    # dbc.CardBody([
                                    #     html.A("Schwalb: Stream Ecology", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt", "vertical-align":"middle"})
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/blind_salamander.svg",style=IMG_STYLE), 
                                    # dbc.CardBody([
                                    #     html.A("Nowlin: Aquatic Ecology", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt", "vertical-align":"middle"})
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/copopod.svg",style=IMG_STYLE),
                                    # dbc.CardBody([
                                    #     html.A("Another Lab", href="", style={"color":"black"}),
                                    # ]), 
                                ],style={"width":"200pt", "height":"160pt", "vertical-align":"middle"})
                                
                            ],className="card-cols"),
                    ], style={"padding-top":"1rem", "padding-left":"5rem"}),
                ] + 
                    [html.Br()]*50 +
                [dbc.Row([
                    html.P("Projects", id="mid3", style={"font-weight":"bold", "font-size":"28pt", "padding": "1rem",}),
                  ], className="card-cols"),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("Space to highlight projects", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",})
                    ]),
                ] +     
                    [html.Br()]*50 +
                [dbc.Row([
                    html.P("Publications", id="end", style={"font-weight":"bold", "font-size":"28pt", "padding": "1rem", }),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("Space to highlight publications", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem", "margin-bottom":"50rem" })
                    ]),
                dbc.Row([
                    dbc.Col([
                        html.P("© 2021 TRIAGE", style={"margin-top":"1rem"})],),
                        dbc.Col([
                            html.P("Follow us on:", style={"margin-top":"1rem", "text-align":"right", "margin-left":"5rem"}),]),
                            html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
                                children=[
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",)]
                                    ),
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",),
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png"),
                ])
                ]      
                                 ),
    id="page-content", style=CONTENT_STYLE,)




app = dash.Dash( __name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}], suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE], )
server = app.server
app.layout = html.Div([sidebar, content])


if __name__ == "__main__":
    app.run_server(debug=True)