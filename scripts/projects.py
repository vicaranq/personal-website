import dash_core_components as dcc
import dash_html_components as html

def get_projects():

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