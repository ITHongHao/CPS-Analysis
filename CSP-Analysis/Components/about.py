import dash_mantine_components as dmc

class AboutPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("About Page Generated")

    def render(self):
        return dmc.Text("About Page")