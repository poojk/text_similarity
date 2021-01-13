import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import math
from collections import Counter
import os

stop=["is","was","the","it","in","and","or","of","a","an","on","if","to"]

contractions = {"aren't": "are not","can't": "cannot","could've": "could have","couldn't": "could not","didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hasn't": "has not","haven't": "have not","he'll": "he will","how'd": "how did","how'll": "how will","I'll": "I will","I'm": "I am","I've": "I have","isn't": "is not","it'll": "it will","it's": "it is","let's": "let us","ma'am": "madam","mayn't": "may not","might've": "might have","mightn't": "might not","must've": "must have","mustn't": "must not","needn't": "need not","shan't": "shall not","she'll": "she shall / she will","should've": "should have","shouldn't": "should not","that's": "that is","there's": "there is","they'll": "they will","they're": "they are","they've": "they have","to've": "to have","wasn't": "was not","we'll": "we will","we're": "we are","we've": "we have","weren't": "were not","what'll": "what will","what're": "what are","what's": "what is","what've": "what have","when's": "when is","when've": "when have","where'd": "where did","where's": "where is","where've": "where have","who'll": "who will","who's": "who is","who've": "who have","why've": "why have","will've": "will have","won't": "will not","would've": "would have","wouldn't": "would not","wouldn't've": "would not have","y'all": "you all","y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would","you'd've": "you would have","you'll": "you will","you're": "you are","you've": "you have"}

def word_to_vec(l1, l2):
    dict_l1 = Counter(l1)
    dict_l2 = Counter(l2)
    words = set(dict_l1.keys()).union(set(dict_l2.keys()))
    v1 = [dict_l1[k] for k in words]
    v2 = [dict_l2[k] for k in words]
    return v1, v2

def cosine_similiarity(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2))
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)

def remove_contractions(l1):
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
    out=[]
    l1 = sentence.lower().split(" ")
    l1 = [word.replace(".", "") for word in l1]
    for word in l1:
        if word not in stop:
            out.append(word)
    return remove_contractions(out)  

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
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

@app.callback(Output('c', 'value'),
        [Input('a', 'value'),
        Input('b', 'value')])
def crux(a,b):
    v1, v2 = word_to_vec(format_text(a), format_text(b))
    x = round(cosine_similiarity(v1, v2),2)
    return x    

if __name__ == "__main__":
    app.run_server(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)))
    
#if __name__ == '__main__':
#    app.run_server(debug=True)


