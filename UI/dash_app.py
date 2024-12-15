import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import random
import os

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the question-answer pairs from the file
def load_q_a_pairs():
    if os.path.exists("q_a_pairs.txt"):
        with open("q_a_pairs.txt", "r") as f:
            lines = f.readlines()
        q_a = [tuple(line.strip().split("\t")) for line in lines]
        return q_a
    else:
        return [("No questions available", "Please generate flashcards in the Streamlit app.")]

q_a = load_q_a_pairs()

# Shuffle questions for randomness
random.shuffle(q_a)

# App layout
app.layout = html.Div([
    html.H1("Flashcard App", style={'textAlign': 'center'}),
    html.Div(id='question-container', style={
        'fontSize': '20px', 
        'margin': '20px 0',
        'border': '2px solid #000',
        'padding': '10px',
        'borderRadius': '5px',
        'width': '500px', 
        'height': '50px',  # Adjust height as needed
        'textAlign': 'center',  # Horizontally center text
        'marginLeft': 'auto',
        'marginRight': 'auto',
        'display': 'flex',  # Use flexbox
        'alignItems': 'center',  # Vertically center text
        'justifyContent': 'center',  # Horizontally center text
    }), 
    html.Div(id='answer-container', style={
        'display': 'flex',
        'justifyContent': 'center',
        'color': 'green',
        'margin-top': '10px',
        'fontSize': '18px',
        'border': '2px solid #000',
        'padding': '10px',
        'borderRadius': '5px',
        'width': '500px',
        'height': '50px',
        'textAlign': 'center',
        'marginLeft': 'auto',
        'marginRight': 'auto',
        'alignItems': 'center',  # Vertically center the text in answer box
    }),
    html.Div([
        html.Button("Next", id='next-btn', n_clicks=0),
        html.Button("Show Answer", id='show-answer-btn', n_clicks=0)
    ], style={'display': 'flex', 'gap': '10px', 'marginTop': '10px', 'justifyContent': 'center'})
], style={
    'display': 'flex',
    'flexDirection': 'column',
    'alignItems': 'center',
    'height': '100vh',  # Fill the height of the page
    'textAlign': 'center',  # This will only apply to the heading
    'justifyContent': 'center'
})

# Single callback to handle next and show answer
@app.callback(
    [Output('question-container', 'children'),
     Output('answer-container', 'children')],
    [Input('next-btn', 'n_clicks'),
     Input('show-answer-btn', 'n_clicks')],
    prevent_initial_call=True
)
def update_flashcard(next_clicks, show_answer_clicks):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    current_idx = (next_clicks or 0) % len(q_a)
    question, answer = q_a[current_idx]
    
    if trigger_id == 'show-answer-btn' and show_answer_clicks > 0:
        return (
            html.Div(question),
            html.Div(answer)
        )
    
    return (
        html.Div(question),
        html.Div("")
    )

if __name__ == '__main__':
    app.run_server(debug=True)
