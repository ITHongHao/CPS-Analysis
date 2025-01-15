import dash_mantine_components as dmc
from Components.table import Table
from dash import dash_table, dcc, html


# displays all information and statistical tests
class DataPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Data component Generated")

    def render(self):
        return dmc.Container([
            dmc.Title("Data Viewer", order=2),
            dcc.Dropdown(
                id="data-dropdown",
                options=[{"label": "Table 1", "value": "table1"}, {"label": "Table 2", "value": "table2"}],
                placeholder="Select a data table",
                style={"marginBottom": "20px"}
            ),
            dash_table.DataTable(
                id="data-table",
                columns=[{"name": "Column 1", "id": "col1"}, {"name": "Column 2", "id": "col2"}],
                data=[],
                style_table={"overflowX": "auto"}
            )
        ])
