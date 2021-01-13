print ("Hello")

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import math
from collections import Counter

stop=["is","was","the","it","in","and","or","of","a","an","on","if","to"]

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

def format_text(sentence):
    out=[]
    l1 = sentence.lower().split(" ")
    l1 = [word.replace(".", "") for word in l1]
    for word in l1:
        if word not in stop:
            out.append(word)
    return out

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

if __name__ == '__main__':
    app.run_server(debug=True)
    
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
