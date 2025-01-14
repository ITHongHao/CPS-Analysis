import dash_mantine_components as dmc

class Table:
    def __innit__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Table component generating")

    def render(self):
        return dmc.Stack([
            dmc.Text("Data Table")
        ])
