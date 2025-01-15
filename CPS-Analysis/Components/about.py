import dash_mantine_components as dmc

class AboutPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("About Page Generated")

    def render(self):
        return dmc.Container([
            dmc.Title("About This Project", order=2),
            dmc.Text(
                "This project was created to analyze CPS data interactively and provide meaningful insights "
                "through dashboards, maps, and tables.",
                style={"marginTop": "20px"}
            ),
            dmc.Text(
                "Developed by [Your Name], a passionate developer and data analyst.",
                style={"marginTop": "10px"}
            )
        ])