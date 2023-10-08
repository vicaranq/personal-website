import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from apps import bio
from dash_extensions import Download
from dash_extensions.snippets import send_file
from scripts import projects, photos, contact, util

#pip install scout-apm
# Integrating with scoutapm
from scout_apm.flask import ScoutApm




app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions=True
app.title = "Victor Arango-Quiroga"
application = app.server # for AWS

# flask_app = app.server

# # Setup as per Flask integration
# ScoutApm(flask_app)
# flask_app.config["SCOUT_NAME"] = "website-monitoring"


colors = {
            'background': '#111111',
                'text': '#008B8B',
                'title': '#4682B4'
        }


def generate_row_header():
    return  \
        dbc.Row([
            dbc.Col(
                [html.Img(src=app.get_asset_url('me.jpg'), style={'height':'100%', 'width':'100%'})] , width=4
            ),
            dbc.Col([
                    html.H1(children='Victor Arango-Quiroga', style={'textAlign':'center', 'font-style': 'italic' }), #, 'color': colors['title']
                    html.H3(children='Machine Learning Engineer', style={'textAlign':'center'}),
                    html.H3(children='Tech Lead', style={'textAlign':'center'})
                ],width=8, className = "h-50", align="center"),

        ])
   
def get_tabs():
    return \
         html.Div([
            dcc.Tabs(id="tabs", value='tab-1-bio', children=[                
                dcc.Tab(label='Bio', value='tab-1-bio'),
                dcc.Tab(label='Projects', value='tab-2-projs'),
                dcc.Tab(label='Photos', value='tab-3-pics'),
                dcc.Tab(label='Contact', value='tab-4-contact')
            ]),
        ])

app.layout = dbc.Container(
    [
        html.Br(),
        generate_row_header(),
        html.Br(),
        get_tabs(),
        html.Div(id='tabs-content'),
    ]
)

######## CALLBACKS #########
#### PROJECTS ######
@app.callback(Output("output", "children"), 
                [Input("input", "value")], 
                prevent_initial_call=True)
def output_text(review):
    return util.predict(review)

@app.callback(Output("word_sim_output", "children"), 
                [Input("word_sim_input", "value")], 
                prevent_initial_call=True)
def output_text(word):
    return util.getSimilarity(word.strip().lower())

#### BIO ######
@app.callback(
    Output("download", "data"), 
    [Input("btn", "n_clicks")],
    prevent_initial_call=True)
def func(n_clicks):
    return send_file("assets/CV/Arango-Quiroga_Victor_CV.pdf")
#### APP ######
@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1-bio':
        return bio.get_bio_content(app)
    elif tab == 'tab-2-projs':
        return projects.get_projects(app)
    elif tab == 'tab-3-pics':
        return photos.get_photos(app)
    elif tab == 'tab-4-contact':
        return contact.get_contact_info()             



if __name__ == '__main__':
    #app.run_server(debug=True)
    application.run(debug=True, port=8080) # for AWS

