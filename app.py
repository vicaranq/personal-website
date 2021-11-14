import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from scripts import projects, photos, contact
import dash_bootstrap_components as dbc
from apps import bio
# import base64
from flask import Flask,send_from_directory



server = Flask(__name__)
app = dash.Dash(server=server)
# app = dash.Dash(__name__)
app.title = "Victor Arango-Quiroga"
# server = app.server

colors = {
            'background': '#111111',
                'text': '#008B8B'
        }

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
            plot_bgcolor=colors['background'],
                paper_bgcolor=colors['background'],
                    font_color=colors['text']
                    )

app.layout = html.Div(children=[
    # html.H1(children='Victor Arango-Quiroga',
    #         style={'textAlign':'center', 'color':colors['text']}),

    # html.Div(children='Machine Learning Engineer',
    #         style={'textAlign':'center', 'color':colors['text']}),

    # # first column of first row
    # html.Div(children="Testing1", style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '100px', 'margin-top': '3vw'}),

    # # second column of first row
    # html.Div(children="Testing2", style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '100px', 'margin-top': '3vw'}),

    # # third column of first row
    # html.Div(children="Testing3", style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '100px', 'margin-top': '3vw','width': '100%'}),
    
    # first row
    html.Div(children=[

        # first column of first row
        html.Div(html.Img(src=app.get_asset_url('me.jpg'), style={'height':'75%', 'width':'85%'}), 
            style={'display': 'inline-block', 'width':'33%','textAlign':'center', "border":"2px black solid"}), #, 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),

        # second column of first row
        html.Div(children= 
        # "test"
        [
            html.H1(children='Victor Arango-Quiroga',  style={'textAlign':'text-top', 'width':'100%', 'color':colors['text'], "border":"2px black solid"}),
            html.H3(children="Machine Learning Engineer", style={'width':'100%','textAlign':'center', 'color':colors['text'], "border":"2px black solid"}), #, 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
        ]
        , 
            style={'display': 'inline-block', 'height' :'100px' ,'width':'33%', "border":"2px black solid", 'textAlign':'center'})

        # third column of first row
        # html.Div(children="Testing3", style={'display': 'inline-block', 'width':'33%','textAlign':'center'}), #, 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),

    ], className='row', style={ 'width': '100%', "border":"2px black solid"}),

    # dbc.Row(
    #     [
    #         dbc.Col(html.Div("One of three columns"), width=2),
    #         dbc.Col(html.Div("One of three columns"), width=2),
    #         dbc.Col(html.Div("One of three columns"), width=2),
    #     ]
    # ),    


    dcc.Tabs(id="tabs-example-graph", value='tab-1-bio', children=[
        dcc.Tab(label='Bio', value='tab-1-bio'),
        dcc.Tab(label='Projects', value='tab-2-projs'),
        dcc.Tab(label='Photos', value='tab-3-pics'),
        dcc.Tab(label='Contact', value='tab-4-contact')
    ]),
    html.Div(id='tabs-content-example-graph')
])



@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-bio':
        return bio.get_bio_content()
    elif tab == 'tab-2-projs':
        return projects.get_projects()
    elif tab == 'tab-3-pics':
        return photos.get_photos(app)
    elif tab == 'tab-4-contact':
        return contact.get_contact_info()             

# @server.route("/Download/<path:path>")
# def download(path):
#     return send_from_directory('', path, as_attachment=True)
    

if __name__ == '__main__':
    app.run_server(debug=True)

