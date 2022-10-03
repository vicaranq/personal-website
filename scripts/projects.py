import dash_core_components as dcc
import dash_html_components as html

import dash_bootstrap_components as dbc
from dash import html

from scripts import util

def get_projects():

    return html.Div([
            html.Br(),
            html.H3('In progress...'),
            html.Br(),
            # sentiment_analysis_card,
            # word_similarity,
            cards,


        ])



''' ------------------------------- CARDS ------------------------------- '''

sentiment_analysis_card = dbc.Card(
                            [

                                dbc.CardBody(
                                    [
                                        html.H4("Sentiment Analysis", className="card-title"),
                                        html.P(
                                            """For this project, I developed a binary linear classifier that reads movie reviews and guesses whether they are “positive” or “negative”.
                                            The  data used for developing this project was obtained from www.rottentomatoes.com.
                                            
                                            I implemented this algorithm using stochastic gradient descent and learned the predictor by minimizing the hinge loss function. The generated 
                                            predictor obtained a training error of 0.027011 and test error of 0.2751228. For this project, I utilized a sparse feature vector represented in 
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


word_segmentation_1 = dbc.Card(
                            [

                                dbc.CardBody(
                                    [
                                        html.H4("Word Segmentation 2", className="card-title"),
                                        html.P(
                                            """
                                            I develoepd an algorithm to find the optimal word segmentation of an input character sequence. The input string must be a string of alphabetical characters
                                            without whitespaces. For instance, for input "thisisatest" we should obtain "this is a test". The Uniform Cost Search algorithm is used to 

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


word_similarity = dbc.Card(
                            [

                                dbc.CardBody(
                                    [
                                        html.H4("Word Similarity", className="card-title"),
                                        html.P(
                                            """
                                            I develoepd a Vector Space Model (VSM) based on the Gigaword dataset with window size of 5 and scaled. Furthermore, I reweighted the matrix using the Positive Pointwise Mutual Information (PPMI) and 
                                            used the Latent Semantic Analysis (LSA) dimensionality reduction technique. Based on an input word, one could find the closest words to it (e.g. similar words). Please provide a word and this 
                                            program will show the 5 closest words to it according to this VSM. 
                                            Note: Word examples are: terrific, happy, dance, sleep.  
                                            """,
                                            className="card-text", 
                                            style = {'align' : 'justify'}

                                        )
                                    ]
                                ),
                                html.Div(
                                    [
                                        dbc.Input(id="word_sim_input", placeholder="Type input word...", type="text"),
                                        html.Br(),
                                        html.P(id="word_sim_output"),
                                    ]
                                ),                                
                            ],
                            style={"width": "24rem"},
                        )

# NLP: final project

bert_tweet_proj = dbc.Card(
                            [

                                dbc.CardBody(
                                    [
                                        html.H4("RecoTweet", className="card-title"),
                                        html.P(
                                            """
                                            This was my final project for the XCS224U: Natural Language Understanding  class at Standford University. In this project, I worked with 
                                            Elizabeth Yam, I current Google engineer. 


                                            A set of experiments on sentiment analysis
                                            datasets were performed to compare two embedding
                                            models, BERT and BERTweet. We
                                            are using the BERTweet-large model which
                                            was pretrained with 873M English cased
                                            Tweets. Our hypothesis was that BERTweet
                                            would outperform the BERT model on tweets
                                            due to the different data that each model was
                                            trained on (e.g. well-structured text vs informal
                                            text from tweets). Our findings indicate
                                            that the BERTweet model has the same
                                            or slightly better results over BERT when we
                                            compare them using datasets containing Twitter
                                            data. As part of this project, we are also using
                                            a pre-built named entity recognition (NER)
                                            model to create a general system to perform
                                            sentiment analysis on products from a dataset
                                            of tweets.

                                            """,
                                            className="card-text", 
                                            style = {'align' : 'justify'}

                                        ),
                                        dbc.Button("Final Paper", color="link", href="https://github.com/vicaranq/CS224-final-project/blob/main/xcs224u_final_paper.pdf", target="_blank"),
                                    ]
                                ),                              
                            ],
                            style={"width": "24rem"},
                        )                        

# ------------------------- DEFINE CARDS LAYOUT  --------------------

cards = html.Div(
    [
        dbc.Row(
        [
            dbc.Col(sentiment_analysis_card, width="auto"),
            dbc.Col(word_similarity, width="auto"),
        ]
        ),
        dbc.Row(
        [
            dbc.Col(bert_tweet_proj, width="auto"),
            #dbc.Col(word_similarity, width="auto"),
        ]
        ),

    ]
    )
''' ------------------------------- END CARDS ------------------------------- '''


'''
class SegmentationProblem(util.SearchProblem):
    def __init__(self, query, unigramCost):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        pass
        # ### START CODE HERE ###
        return (0,0) 
        # ### END CODE HERE ###

    def isEnd(self, state):
        pass
        # ### START CODE HERE ###
        return state[1] >= len(self.query) # Current state has finalized capturing the query string
        # ### END CODE HERE ###

    def succAndCost(self, state):
        pass
        # ### START CODE HERE ###
        start_idx, end_idx = state 
        # First time, end_idx will be 0 from initial state, next values will depend on the lowest cost in succesor list which is returned in this function
        N = len(self.query)        
        return [(self.query[end_idx:j] , (end_idx, j), self.unigramCost(self.query[end_idx:j])) for j in range(end_idx+1, N+1)]
        # ### END CODE HERE ###

def segmentWords(query, unigramCost):
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # ### START CODE HERE ###
    return " ".join(ucs.actions)
    # ### END CODE HERE ###    

def get_segmented_word(input_seq):    
    def unigramCost(x):
        if x in ['this', 'is', 'a', 'test']:
            return 1.0
        else:
            return 1000.0
    return segmentWords(input_seq, unigramCost)    
    '''