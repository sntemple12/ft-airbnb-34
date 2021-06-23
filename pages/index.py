# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### How much is your property worth?
            
            
            This app is built to help hosts predict the price of their daily rental price. Please
            fill out the form as accurately as possible. We will compare similar properties and
            provide you with the best estimate for the daily rental price. 
            """,
            style={'fontFamily':'Verdana', 'fontWeight': 'normal', 'fontSize': 'smaller'}
        ),
        dcc.Link(dbc.Button('Predict That Price', color='primary'), href='/predictions'),

    ],
    md=6,
)

column2 = dbc.Col(
    [
       html.Img(src='assets/airbnb5.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])