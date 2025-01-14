import dash_mantine_components as dmc
from Components.summary import Summary


# displays all information and statistical tests
class DashboardPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        self.summary = Summary(self.app)

    def render(self):
        return dmc.Stack([
            dmc.Text("CPS Data Dashboard"),
            self.summary.render(),  # Including the summary section in the dashboard
        ])
