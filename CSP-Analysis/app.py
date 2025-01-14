import dash
import dash_mantine_components as dmc
from Components.home import HomePage


app = dash.Dash(__name__)
app.layout = dmc.MantineProvider(HomePage(app).render())


if __name__ == "__main__":
    app.run_server(debug=True)
