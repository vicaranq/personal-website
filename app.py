import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import base64



app = dash.Dash(__name__)
app.title = "Victor Arango-Quiroga"
server = app.server

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
    html.H1(children='Victor Arango-Quiroga',
            style={'textAlign':'center', 'color':colors['text']}),

    html.Div(children='Machine Learning Engineer',
            style={'textAlign':'center', 'color':colors['text']}),

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
        with open('files/bio.txt') as f:
            bio = f.read()
        return html.Div([
                dcc.Markdown(bio)
                 ])

    elif tab == 'tab-2-projs':
        return html.Div([
            html.H3('Comming soon!...'),
            dcc.Graph(
                id='graph-1-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [3, 1, 2],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-3-pics':
        return html.Div([
                        html.H4('These are some of my favorite pictures that I have taken:'),

                        html.Div([html.Img(src=app.get_asset_url('pic2.jpg'), style={'height':'50%', 'width':'50%'}),
                                  html.Img(src=app.get_asset_url('pic4.jpg'), style={'height':'50%', 'width':'50%'}) 
                                  ]),
                        html.Div([html.Img(src=app.get_asset_url('pic5.jpg'), style={'height':'50%', 'width':'50%'}),
                                  html.Img(src=app.get_asset_url('pic6.jpg'), style={'height':'50%', 'width':'50%'}) 
                                  ]), 
                        html.Div([html.Img(src=app.get_asset_url('pic7.jpg'), style={'height':'50%', 'width':'50%'}),
                                  html.Img(src=app.get_asset_url('pic8.jpg'), style={'height':'50%', 'width':'50%'}) 
                                  ]),                                                                       
                        html.Img(src=app.get_asset_url('pic1.jpg'), style={'width':'100%'}),                        
                        html.H3('In progress...'),
                      ])


    elif tab == 'tab-4-contact':
        with open('files/contact.txt') as f:
            contact = f.read()
        return html.Div([
                dcc.Markdown(contact)
                ])              

if __name__ == '__main__':
    app.run_server(debug=True)

