
import dash_core_components as dcc
import dash_html_components as html
from dash_extensions import Download


file_location = "files/bio.txt"

def get_download_row():
    return \
         html.Div([
            html.H3("Resume/CV"),
            html.Div([html.Button("Download resume/CV", id="btn"), Download(id="download")]), # Note: Callback handle in app.py
            html.Br()
        ])

def get_bio_content():

    try: 
        with open(file_location) as f:
            bio = f.read()
        return html.Div([
                html.Br(),
                dcc.Markdown(bio),              
                get_download_row()                
                ])
    except Exception as e: 
        print(f"Error when tring to read BIO information from [{file_location}]. Exception: {e}")
        raise                    