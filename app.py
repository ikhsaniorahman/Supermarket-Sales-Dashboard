import dash
import dash_bootstrap_components as dbc

# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.MINTY]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Supermarket Dashboard - Milestone 1"

server = app.server
app.config.suppress_callback_exceptions = True
