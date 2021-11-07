
import dash_core_components as dcc
import dash_html_components as html

file_location = 'files/bio.txt'

# @app.callback(
#     Output("download-text", "data"),
#     Input("btn-download-txt", "n_clicks"),
#     prevent_initial_call=True,
# )
# def func(n_clicks):
#     return dict(content="Hello world!", filename="hello.txt")


def get_bio_content():
    try: 
        with open(file_location) as f:
            bio = f.read()
        return html.Div([
                dcc.Markdown(bio)
                ])
    except Exception as e: 
        print(f"Error when tring to read BIO information from [{file_location}]. Exception: {e}")
        raise                    
