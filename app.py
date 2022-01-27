
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
    "min-height": "100%",
    "display": "grid",
    "grid-template-rows": "auto 1fr auto",
    "grid-template-columns": "100%"
}
HEADER_STYLE = {
    "font-weight":"bold", 
    "font-size":"28pt", 
    "padding": "1rem"
}

CARD_ROW = {
    
    "display":"flexbox", 
    "padding":"1rem",
    "margin":"0 auto", 
    "text-align":"center", 
    "row-gap": "2rem",
    "object-fit": "cover",
    "justify-items": "center"

}
IMG_STYLE = {
    "margin-top":"1rem",
    "color":"black", 
    "width":"160pt", 
    "height":"120", 


}

CARD_STYLE = {
    "display": "block",
    "margin-left":"3rem",
    "justify-content":"center",
    "vertical-align":"middle",
    "width":"200pt", 
    "height":"160pt",

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
                dbc.NavLink("Home", style={"color":"white", "font-size":"12pt"}, href="#home", external_link=True,),
                dbc.NavLink("About", style={"color":"white", "font-size":"12pt"}, href="#about",external_link=True),
                dbc.NavLink("Teams", style={"color":"white", "font-size":"12pt"}, href="#teams",external_link=True),
                dbc.NavLink("Projects", style={"color":"white", "font-size":"12pt"}, href="#projects",external_link=True),
                dbc.NavLink("Publications", style={"color":"white", "font-size":"12pt"}, href="#publications",external_link=True),
                # html.P('Developed by: Bianca A. Hernandez', style={"font-size": "8pt", "margin-top":"28rem", "text-align":"center"}),
                html.P("T", className="MINI_LOGO")
                
        ],
            vertical=True,
            pills=True,
        ),
    ],
    className="SIDEBAR_STYLE"
)

content = html.Div(
            html.Div([
                dbc.Row(id="home", style={"height":"25rem","background-image":"url('assets/rio-grande-river.jpg')", "background-position":"center center", "border":"black",}),
                dbc.Row([
                    html.P("Texas Research Institute for Aquatic & Groundwater Ecology", style=HEADER_STYLE),
                  ], style={"justify-content":"center",}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("A cooperative research group centered at Texas State University that examines basic and applied ecological questions in aquatic and groundwater systems.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",}),
                    ]),
                ] +
                # [html.Br()]*50 + 
                [dbc.Row([
                    html.P("Mission & Goals", id="about", style=HEADER_STYLE),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("The climate crisis is affecting and threatening aquatic ecosystems and the benefits and services these systems provide. Our collaborative research aims to better understand and predict the impacts of climatic changes on aquatic communities. A central focus of research is determining the factors underlying the distribution of aquatic organisms and how increased frequency and intensity of hydrological disturbances will affect the ecology of aquatic ecosystems. The key mission of TRIAGE is to contribute to an increase in diversity (visible and invisible) in aquatic sciences by building and maintaining a diverse and inclusive research team, educating and training students from diverse backgrounds, and promoting broader engagement through outreach to the public.", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",})
                    ]),
                ] +           
                [html.Br()]*50 +

                [dbc.Row([
                    html.P("Teams", id="teams", style=HEADER_STYLE),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="/assets/fatmucket.svg", style=IMG_STYLE), 
                            dbc.CardBody([
                                html.A("Schwalb: Stream Ecology", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black", "font-size":"14pt",}), 
                                    ]) 
                                ],style=CARD_STYLE),
                            # dbc.Row([
                            #             html.A("Schwalb: Stream Ecology", href="https://streamecology.wp.txstate.edu/current-students/", style={"color":"black", "font-size":"18pt", "margin-left":"1rem"}), 
                            # ]),
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/ephemeoptera.svg",style=IMG_STYLE),
                                    dbc.CardBody([
                                        html.A("Nowlin: Aquatic Ecology", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black", "font-size":"14pt",}), 
                                    ]) 
                                ],style=CARD_STYLE),
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/microbes.svg",style=IMG_STYLE),
                                    dbc.CardBody([
                                        html.A("Engel: ", href="", style={"color":"black", "font-size":"14pt"}), 
                                    ]),
                                ],style=CARD_STYLE),
                                
                            ],className="card-cols"),
                            ], style=CARD_ROW),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardImg(src="/assets/longnose_dace.svg", style={"margin-top":"3rem", "margin-bottom":"2.8rem", "color":"black", "width":"160pt", "height":"120",}), 
                                dbc.CardBody([
                                        html.A("Perkin: Fish Ecology", href="https://www.riverscapeecology.org/", style={"color":"black", "font-size":"14pt",}), 
                                    ]),    
                                ],style=CARD_STYLE),
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/blind_salamander.svg",style=IMG_STYLE), 
                                    # dbc.CardBody([
                                    #     html.A("Nowlin: Aquatic Ecology", href="https://nowlinaquatecollab.wp.txstate.edu/nowlin-lab-folks/", style={"color":"black"}),
                                    # ]), 
                                ],style=CARD_STYLE)
                            ],className="card-cols"),
                            dbc.Col([
                                 dbc.Card([
                                    dbc.CardImg(src="/assets/copopod.svg",style=IMG_STYLE),
                                    # dbc.CardBody([
                                    #     html.A("Another Lab", href="", style={"color":"black"}),
                                    # ]), 
                                ],style=CARD_STYLE)
                            ],className="card-cols"),
                    ], style=CARD_ROW),
                ] + 
                    [html.Br()]*50 +
                [dbc.Row([
                    html.P("Projects", id="projects", style=HEADER_STYLE),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("Space to highlight projects", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem",})
                    ]),
                ] +     
                    [html.Br()]*50 +
                [dbc.Row([
                    html.P("Publications", id="publications", style=HEADER_STYLE),
                  ], style={"justify-content":"center"}),
                html.Hr([],style={"margin":"0rem"}),
                dbc.Row([
                    html.P("Space to highlight publications", style={"font-size":"18pt","text-align":"justify", "padding": "2rem 1rem", "margin-bottom":"50rem" })
                    ]),
                dbc.Row([
                    html.A(href="https://www.facebook.com/Texas-Research-Institute-for-Aquatic-and-Groundwater-Ecology-104627268475583",
                                children=[
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/facebook-new.png",style={"margin-bottom":"1rem"})]
                                    ),
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/instagram-new.png",style={"margin-bottom":"1rem"}),
                                    html.Img(src="https://img.icons8.com/material-rounded/48/000000/twitter.png", style={"margin-bottom":"1rem"}),
                ], style= {"display":"flexbox", "bottom":"0", "position":"sticky", "width":"100%","justify-content":"right"})
                ], style = {"overflow-y":"hidden"}      
                                 ),
    id="page-content", className="CONTENT_STYLE",)




app = dash.Dash( __name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}], suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.SANDSTONE], )
server = app.server
app.layout = html.Div([sidebar, content])


if __name__ == "__main__":
    app.run_server(debug=True)