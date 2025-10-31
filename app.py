import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load processed sales data
df = pd.read_csv('data/processed_sales.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

# Initialize Dash app
app = Dash(__name__)

# Layout with header, description, and radio buttons
app.layout = html.Div(style={'font-family': 'Arial', 'textAlign': 'center', 'backgroundColor': '#f5f5f5', 'padding': '20px'}, children=[
    html.H1("Pink Morsel Sales Visualiser", style={'color': '#2c3e50'}),
    html.P("Select a region to see sales over time. Price increase occurred on 15th Jan 2021.", 
           style={'color': '#34495e'}),

    # Radio buttons for region filter
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
        ],
        value='all',
        inline=True,
        labelStyle={'margin-right': '15px', 'font-weight': 'bold', 'color': '#34495e'}
    ),

    # Graph
    dcc.Graph(id='sales-line-chart')
])

# Callback to update graph based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region.lower()]
    
    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Sales', 
        color='Region' if selected_region == 'all' else None,
        title='Pink Morsel Sales Over Time',
        labels={'Sales': 'Total Sales', 'Date': 'Date', 'Region': 'Region'},
        template='plotly_white'
    )
    fig.update_layout(title_font_size=22, title_font_color='#2c3e50', 
                      plot_bgcolor='#ecf0f1', paper_bgcolor='#f5f5f5')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
