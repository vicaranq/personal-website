
import dash_core_components as dcc
import dash_html_components as html
# from app import app, server --> circular import issue
# from flask import current_app
from dash.dependencies import Input, Output
from dash_extensions import Download
from dash_extensions.snippets import send_file
from flask import send_from_directory


file_location = "files/bio.txt"
CV_path = "/home/vicaran93/repos/personal_website/files/bio.txt"


def get_bio_content():

    try: 
        with open(file_location) as f:
            bio = f.read()
        return html.Div([
                html.Br(),
                dcc.Markdown(bio),
                # dcc.Markdown("### Resume/CV"),
                # html.A(html.Button('Download file'), href="files/bio.txt")                
                # html.Button("Download CV", id="btn-download-cv"),
                # Download(id="download-cv")
                ])
    except Exception as e: 
        print(f"Error when tring to read BIO information from [{file_location}]. Exception: {e}")
        raise                    

# @app.callback(Output("download-cv", "data"), [Input("btn-download-cv", "n_clicks")])
# def func(n_clicks):
#     return send_file("files/bio.txt")

# @server.route("/files/<path:path>")
# def download(path):
#     return send_from_directory('files', path, as_attachment=True)    

# @app.callback(
#     Output("download-cv", "data"),
#     Input("btn-download-cv", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     return dcc.send_file("assets/pic1.jpg")
    # try:
    #     return dcc.send_file(CV_path)
    # except Exception as e:
    #     print("There was an error downloading CV from [{CV_path}]. Exception: {e}")
    #     raise
