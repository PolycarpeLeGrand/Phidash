import dash_bootstrap_components as dbc


header = dbc.Navbar([
    dbc.Row([
        dbc.Col([
            dbc.NavbarBrand('Dashboard Title', className='ml-2', style={'font-size': '200%'}),
            # html.Hr(),
            dbc.NavbarBrand('Dashboard subtitle', className='ml-2', style={'font-size': '100%'}),
        ]),
    ])
], color='primary', dark=True)

