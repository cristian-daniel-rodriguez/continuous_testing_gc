import dash
from dash import dcc
from dash import html
import pandas as pd

# Load the test results CSV file into a pandas DataFrame
df = pd.read_csv('test_results.csv')

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Test Results Report'),
    dcc.Graph(
        id='test-results-graph',
        figure={
            'data': [
                {'x': df['name'], 'y': df['duration'], 'type': 'bar', 'name': 'Duration'},
            ],
            'layout': {
                'title': 'Test Duration by Test Name'
            }
        }
    ),
    dcc.Graph(
        id='test-results-pie',
        figure={
            'data': [
                {'labels': ['Passed', 'Failed'], 'values': df['status'].value_counts(), 'type': 'pie', 'name': 'Status'},
            ],
            'layout': {
                'title': 'Test Status'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)