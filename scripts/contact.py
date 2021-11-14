import dash_core_components as dcc
import dash_html_components as html


file_location = "files/contact.txt"

def get_contact_info():
    try:    
        with open(file_location) as f:
            contact = f.read()
        return html.Div([
                html.Br(),
                dcc.Markdown(contact)
                ])   
    except Exception as e:
        print(f"Error when tring to read CONTACT information from [{file_location}]. Exception: {e}")
        raise