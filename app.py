import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from scripts import projects, photos, contact
import dash_bootstrap_components as dbc
from apps import bio





app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])


app.title = "Victor Arango-Quiroga"

colors = {
            'background': '#111111',
                'text': '#008B8B',
                'title': '#4682B4'
        }

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
def generate_row_header():
    return  \
        dbc.Row([
        dbc.Col(
            [html.Img(src=app.get_asset_url('me.jpg'), style={'height':'100%', 'width':'100%'})] , width=4
        ),
        dbc.Col([
                html.H1(children='Victor Arango-Quiroga', style={'textAlign':'center', 'color': colors['title'], 'font-style': 'italic' }),
                html.H3(children='Machine Learning Engineer', style={'textAlign':'center', 'color':colors['title']})
            ],width=8, className = "h-50", align="center"),

        ])
   
app.layout = dbc.Container(
    [
        html.Br(),
        generate_row_header(),
        html.Br(),
        
        dcc.Tabs(id="tabs-example-graph", value='tab-1-bio', children=[
            
            dcc.Tab(label='Bio', value='tab-1-bio'),
            dcc.Tab(label='Projects', value='tab-2-projs'),
            dcc.Tab(label='Photos', value='tab-3-pics'),
            dcc.Tab(label='Contact', value='tab-4-contact')
        ]),

        html.Div(id='tabs-content-example-graph')

    ]
)


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

