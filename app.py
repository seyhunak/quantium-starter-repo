# app.py
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed sales data
df = pd.read_csv('data/processed_sales.csv')

# Make sure the Date column is datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Create line chart
fig = px.line(df, x='Date', y='Sales', color='Region', 
              title='Pink Morsel Sales Over Time',
              labels={'Sales': 'Total Sales', 'Date': 'Date', 'Region': 'Region'})

# Initialize Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Visualiser'),
    
    html.P(children='Visualising sales before and after the price increase on 15th Jan 2021.'),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)