import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc
from dash import html


def get_projects():

    return html.Div([
            html.Br(),
            html.H3('In progress...'),
            html.Br(),
            sentiment_analysis_card

        ])


sentiment_analysis_card = dbc.Card(
                            [

                                dbc.CardBody(
                                    [
                                        html.H4("Sentiment Analysis", className="card-title"),
                                        html.P(
                                            """For this project, I developed a binary linear classifier that reads movie reviews and guesses whether they are “positive” or “negative”.
                                            The  data used for developing this project was obtained from www.rottentomatoes.com.
                                            
                                            I implemented this algorithm using stochastic gradient descent and learned the predictor by minimizing the hinge loss function. The generated 
                                            predictor obtained a training error of 0.027011 and test error of 0.2751228. For this project I utilized a sparse feature vector represented in 
                                            Python by a dictionary (e.g. defaultdict from Collections).

                                            I created and used two type of feature extractors in this project; a word feature extractor and a character n-grams feature extractor. The former 
                                            one takes words as features, the latter one takes N characters slices of the review (with no spaces). 

                                            To try it out, get some reviews from https://www.rottentomatoes.com/m/minari/reviews and type it below, a positive or negative prediction will be generated below.

                                            """,
                                            className="card-text", 
                                            style = {'align' : 'justify'}

                                        )
                                    ]
                                ),
                                html.Div(
                                    [
                                        dbc.Input(id="input", placeholder="Type review...", type="text"),
                                        html.Br(),
                                        html.P(id="output"),
                                    ]
                                ),                                
                            ],
                            style={"width": "24rem"},
                        )

