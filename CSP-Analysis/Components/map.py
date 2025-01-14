import dash_mantine_components as dmc

class MapPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Map Page generated")


    def render(self):
        return dmc.Stack([
            dmc.Text("Map Page")
        ])