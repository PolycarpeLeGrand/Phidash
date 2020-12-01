import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashapp import app, DATA
from dashapp.header import header


tabs = dbc.Tabs(
    [
        dbc.Tab(label="Metadonnees", label_style={'cursor': 'pointer'}),
        dbc.Tab(label="Lexique", label_style={'cursor': 'pointer'}),
        dbc.Tab(label="Topic Modeling", label_style={'cursor': 'pointer'}),
        dbc.Tab(label="Tables", label_style={'cursor': 'pointer'}),
    ], id='tabs', active_tab='tab-0', style={'padding-left': '10px', }
)


layout = html.Div([
    dcc.Location(id='url', refresh=False),
    header,
    html.Div([
        tabs,
    ], className='pt-2 bg-dark text-light'),
    dbc.Container([], id='tab-container', fluid=True, className='bt-2 pt-3'),

])




