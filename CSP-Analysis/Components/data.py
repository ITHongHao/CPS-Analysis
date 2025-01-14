import dash_mantine_components as dmc
from Components.table import Table


# displays all information and statistical tests
class DataPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Data component Generated")

    def render(self):
        return dmc.Stack([
            dmc.Text("CPS Data"),
        ])
