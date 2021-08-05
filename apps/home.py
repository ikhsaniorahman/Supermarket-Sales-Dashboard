from dash_bootstrap_components._components.Col import Col
from dash_bootstrap_components._components.Row import Row
import plotly.express as px
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

# Data Preprocessing
df = pd.read_csv('supermarket_sales.csv')
df.columns = df.columns.str.lower()
df.drop(['invoice id', 'time', 'rating'], axis=1, inplace=True)
df['date'] = pd.to_datetime(df['date'])
df.rename(columns={'customer type': 'customer_type',
          "product line": "product_line"}, inplace=True)
df1 = df.groupby(["city"]).sum().reset_index()

layout = html.Div([
    dbc.Container([
        # header
        dbc.Row(
            dbc.Col(
                html.H1("Welcome to Supermarket Sales Dashboard!",
                        className="text-center"),
                className="mb-5 mt-5")
        ),
        dbc.Row([
            dbc.Col([
                html.H6(
                    "Hello, I'm M. Ikhsan Rahman and this is my first dash dashboard."),
                html.P(
                    'This dashboard contains an analysis of the sales of a supermarket in Myanmar for 3 months in 2019.'),
            ], className="mb-4")
        ]),

        # card
        dbc.CardDeck([
            dbc.Card([
                dbc.CardImg(src=app.get_asset_url(
                    'rsz_data.png'), top=True, style={"width": "16rem", 'text-align': 'center', 'margin': 'auto'}),
                dbc.CardBody([
                    html.H2(children='Dataset',
                            className="text-center"),
                    html.P(
                        "The dataset originally from kaggle. Click the button below to get the original dataset!",
                        className="card-text text-center",
                    ),
                    dbc.Button("Get the dataset!",
                               href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                               color="info",
                               className="mt-10", block=True),
                ]),
            ],
                body=True, outline=True, style={'text-align': 'center'}
            ),

            dbc.Card([
                dbc.CardImg(src=app.get_asset_url(
                    'rsz_hypothesis.png'), top=True, style={"width": "15.1rem", 'text-align': 'center', 'margin': 'auto'}),
                dbc.CardBody([
                    html.H2(children='Hypothesis',
                            className="text-center"),
                    html.P(
                        "Click button below to know my hypothesis!",
                        className="card-text text-center",
                    ),
                    dbc.Button("See my hypothesis!",
                               href="/apps/page1",
                               color="danger",
                               className="mt-10", block=True),
                ]),
            ],
                body=True, outline=True, style={'text-align': 'center'}
            ),

            dbc.Card([
                dbc.CardImg(src=app.get_asset_url(
                    'Octocat.png'), top=True, style={"width": "16.3rem", 'text-align': 'center', 'margin': 'auto'}),
                dbc.CardBody([
                    html.H2(children='My GitHub',
                            className="text-center"),
                    html.P(
                        "You can find this project by clicking the button below and don't forget to explore my github for more projects!",
                        className="card-text text-center",
                    ),
                    dbc.Button("Find my other project!",
                               href="/apps/page1",
                               color="info",
                               block=True),
                ]),
            ],
                body=True, outline=True, style={'text-align': 'center'}
            ),
        ]),

        # graph utama
        dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        figure=px.bar(
                            df1, x="city", y="total", color="city",
                            title="Total sales per city"
                        )
                    ),
                    className="mb-5"
                )
                ]),

        # chart - total-customertype
        dbc.Spinner([
            dbc.Row([
                dbc.Col(
                    html.H2(
                        children='Summary of Total Sales'),
                    className="text-center mb-4"
                )
            ]),
            dbc.Row([
                dbc.Col(
                    html.Div(
                        children=[
                            dcc.Dropdown(
                                id='filter3',
                                options=[
                                    {'label': city, 'value': city} for city in df.city.unique()
                                ],
                                value='Yangon',
                                clearable=False
                            ),
                        ]
                    ),
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id='third-graph'
                    ), className="mb-2"
                )
            ]),

            # pie chart - gender
            dbc.Row([
                dbc.Col(
                    dcc.Dropdown(
                        id='gender',
                        options=[
                            {"label": gender, "value": gender} for gender in df.gender.unique()

                        ],
                        value='Male',
                        clearable=False
                    ),
                    className="mb-4"
                )
            ]),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id='graph_pie'
                    )
                )
            ]),

            # chart  - total-payment
            dbc.Row([
                dbc.Col(
                    html.Div(
                        children=[
                            dcc.Dropdown(
                                id='filter4',
                                options=[
                                    {'label': payment, 'value': payment} for payment in df.payment.unique()
                                ],
                                value='Cash',
                                clearable=False
                            ),
                        ]
                    ),
                ),
            ]),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id='fourth-graph'
                    )
                )
            ])
        ], color="info", type="grow")
    ])
])


# CALLBACK SECTION

@app.callback(  # callback chart total-customer type
    Output('third-graph', 'figure'),
    Input('filter3', 'value')
)
def update_bar_chart(city):
    d1 = df.groupby(['customer_type', 'city'])['total'].sum().reset_index()
    d2 = d1[d1['city'] == city]
    fig = px.bar(d2, x='customer_type', y='total', color="customer_type",
                 barmode="group", title="Total sales per customer type from " + city)
    return fig


@app.callback(  # callback piechart
    Output('graph_pie', 'figure'),
    Input('gender', 'value')
)
def update_graph(gender):
    d3 = df.groupby(['product_line', 'gender'])['total'].sum().reset_index()
    d4 = d3[d3['gender'] == gender]
    piechart = px.pie(d4, names='product_line', values='total',
                      height=600, title="Total sales per product line based on " + gender)
    return piechart


@app.callback(  # callback chart total-payment
    Output('fourth-graph', 'figure'),
    Input('filter4', 'value')
)
def update_bar_chart(payment):
    d1 = df.groupby(['gender', 'payment'])['total'].sum().reset_index()
    d2 = d1[d1['payment'] == payment]
    fig = px.bar(d2, x='gender', y='total', color="gender",
                 barmode="group", title="Total sales per Gender based on their payment (" + payment + ")")
    return fig
