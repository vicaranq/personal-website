import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from scripts import bio, projects, photos, contact
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
        return bio.get_bio_content()
    elif tab == 'tab-2-projs':
        return projects.get_projects()
    elif tab == 'tab-3-pics':
        return photos.get_photos(app)
    elif tab == 'tab-4-contact':
        return contact.get_contact_info()             

if __name__ == '__main__':
    app.run_server(debug=True)

