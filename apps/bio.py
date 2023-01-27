
#import dash_core_components as dcc
from dash import dcc
#import dash_html_components as html
from dash import html
from dash_extensions import Download

file_location = "files/bio.txt"

def get_download_row():
    return \
         html.Div([
            html.H3("Resume/CV"),
            html.Div([html.Button("Download resume/CV", id="btn"), Download(id="download")]), # Note: Callback handle in app.py
            html.Br()
        ])

def get_bio_content(app):

    try: 
        hobbies = '''### Hobbies:\nTravel, soccer (futbol), volleyball, hiking, camping.   '''
        with open(file_location) as f:
            bio = f.read()
        return html.Div([
                html.Br(),                
                dcc.Markdown(bio),   
                # get RPI image
                html.Img(src=app.get_asset_url('Me_RPI.JPG'), style={'height':'30%', 'width':'30%'}),
                dcc.Markdown("*Holding a Dockiebot which I used throughout my research internship at RPI*"),
                dcc.Markdown(hobbies), 
                get_download_row()                
                ], style={'width':'80%', 'margin':25, 'textAlign': 'justify'})
    except Exception as e: 
        print(f"Error when tring to read BIO information from [{file_location}]. Exception: {e}")
        raise                    