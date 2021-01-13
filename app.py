'''
Dash app code snippet to determine the similarity between texts.
Input: s1(string), s2(string)
Output: similarity (int[0-1]) 
'''

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask
import math
from collections import Counter
import os

#list of commonly used stop words
stop=["is","was","the","it","in","and","or","of","a","an","on","if","to"]

#dictionary with contraction words and their actual words
contractions = {"aren't": "are not","can't": "cannot","could've": "could have","couldn't": "could not","didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hasn't": "has not","haven't": "have not","he'll": "he will","how'd": "how did","how'll": "how will","I'll": "I will","I'm": "I am","I've": "I have","isn't": "is not","it'll": "it will","it's": "it is","let's": "let us","ma'am": "madam","mayn't": "may not","might've": "might have","mightn't": "might not","must've": "must have","mustn't": "must not","needn't": "need not","shan't": "shall not","she'll": "she shall / she will","should've": "should have","shouldn't": "should not","that's": "that is","there's": "there is","they'll": "they will","they're": "they are","they've": "they have","to've": "to have","wasn't": "was not","we'll": "we will","we're": "we are","we've": "we have","weren't": "were not","what'll": "what will","what're": "what are","what's": "what is","what've": "what have","when's": "when is","when've": "when have","where'd": "where did","where's": "where is","where've": "where have","who'll": "who will","who's": "who is","who've": "who have","why've": "why have","will've": "will have","won't": "will not","would've": "would have","wouldn't": "would not","wouldn't've": "would not have","y'all": "you all","y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would","you'd've": "you would have","you'll": "you will","you're": "you are","you've": "you have"}

def word_to_vec(l1, l2):
    '''
    Input: Formatted input strings as lists
    Output: Vector representations of the input texts
    Function: Converts the input strings into their vector representations. The vectors consist of 0s and 1s 0 indicating the absence and 1 indicating the presence of the word. 
    '''
    dict_l1 = Counter(l1)
    dict_l2 = Counter(l2)
    words = set(dict_l1.keys()).union(set(dict_l2.keys()))
    v1 = [dict_l1[k] for k in words]
    v2 = [dict_l2[k] for k in words]
    return v1, v2

def cosine_similiarity(v1, v2):
    '''
    Input: Vectors of the input strings.
    Output: Cosine similarity between the input strings.
    Function: Calculates the cosine similarity using the dot product between the two vectors divided by the magnitude of them.
    '''
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2))
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)

def remove_contractions(l1):
    '''
    Input: List of words in the input string.
    Output: List of words from the input string by removing contractions.
    Function: Compares the word with the key values of the dictionary and changes it into the non contracted version of the word.
    '''
    form=[]
    for word in l1:
        if word in contractions.keys():
            f=contractions[word]
            form.append(f.split(" ")[0])
            form.append(f.split(" ")[1])
        else:
            form.append(word)
    return form          

def format_text(sentence):
    '''
    Input: Input sentence in teh form of string.
    Output: List with all the words in the words in teh input sentence after removing stop words and contractions.
    Function: Splits the sentence based on whitespaces, removes punctuations, stop words and contractions using respectively defined functions.
    '''
    out=[]
    l1 = sentence.lower().split(" ")
    l1 = [word.replace(".", "") for word in l1]
    for word in l1:
        if word not in stop:
            out.append(word)
    return remove_contractions(out)  

server = Flask(__name__)    #making use of flask server to run teh app
app = dash.Dash(server=server)    #dash deploys the app and presents it in the front end

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
         }

#layot of teh app in the front end
app.layout = html.Div(children=[
    html.Div(children=[html.H1(children="Text Similiarity",
        style={
            'textAlign': 'center',
            "background": "yellow"})
        ]
        ),
    html.H4(children='Enter Sample Text 1:'),
    dcc.Textarea(id='a',value=' ',style={'width': '100%', 'height': 70}),
    html.H4(children='Enter Sample Text 2:'),
    dcc.Textarea(id='b',value=' ', style={'width': '100%', 'height': 70}),
    html.H4(children='Similiarity between the two texts:'),
    dcc.Input(id='c',value=' ', type='text')
])


#callback function to give the final similarity value.
@app.callback(Output('c', 'value'),
        [Input('a', 'value'),
        Input('b', 'value')])
def crux(a,b):
    '''
    Input: Input strings a and b
    Output: degree of similarity which is between 0 to 1.
    Function: Main function which builds the vector of the two input strings and then calculates the cosine similarity between them and returns it.
    '''
    v1, v2 = word_to_vec(format_text(a), format_text(b))    #after the necessary formatting of teh input strings, v1 and v2 represent their vectors.
    x = round(cosine_similiarity(v1, v2),2)    #the cosine similarity is calculated and is rounded to 2 decimals.
    return x    

if __name__ == "__main__":
    '''
    Function: Main function which calls the app to run on the port 5000 on the local host.
    '''
    app.run_server(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)))

#this main function call can be used to execute the program from cmd line from localhost without specifying teh port number. 
#if __name__ == '__main__':
#    app.run_server(debug=True)


