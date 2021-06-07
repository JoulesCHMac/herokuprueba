import dash
import dash_core_components as dcc
import dash_html_components as html
from navbar import nav
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://eteekin.eus/wp-content/uploads/2018/11/normalize_reset.css','https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div([
                nav(), 
                dcc.Location(id = 'ruta', refresh=False),
                html.Div(id = 'pagina')
])

@app.callback(
    Output('pagina', 'children'), Input('ruta', 'pathname')
)
def display_page(pathname):
    if pathname == '/inicio':
        return [html.H1('Estás en inicio'), html.P('Nuestra introducción, nuestro producto ...')]
    elif pathname == '/about':
        return html.H1('Estás en about')
    else:
        return html.H1('404')

if __name__ == '__main__':
    app.run_server(debug = True)