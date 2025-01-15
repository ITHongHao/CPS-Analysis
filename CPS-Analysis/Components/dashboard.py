import dash_mantine_components as dmc
from Components.summary import Summary
from dash import dcc, html


# displays all information and statistical tests
class DashboardPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        self.summary = Summary(self.app)

    def render(self):
        return dmc.Container([
            dmc.Title("CPS Dashboard", order=2),
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "Sample"}],
                    "layout": {"title": "Sample Chart"}
                }
            )
        ])
