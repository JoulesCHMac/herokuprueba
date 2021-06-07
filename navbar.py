import dash_bootstrap_components as dbc

def nav():
    return dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Inicio", href="/inicio")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Opciones:", header=True),
                dbc.DropdownMenuItem("About", href="/about"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="CdP ESFM",
    brand_href="#",
    color="primary",
    dark=True,
)
