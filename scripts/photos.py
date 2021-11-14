import dash_html_components as html


def get_photos(app):
    return html.Div([
                html.Br(),
                
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