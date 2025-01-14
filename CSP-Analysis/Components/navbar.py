from dash_mantine_components import Tabs, TabsList, TabsTab, TabsPanel
from Components.chatbot import ChatbotPage
from Components.dashboard import DashboardPage
from Components.data import DataPage
from Components.map import MapPage
from Components.about import AboutPage



# creates the navigation bar at the top of the website, routes to each of the pages
class Navbar:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        self.chatbot = ChatbotPage(self.app)
        self.dashboard = DashboardPage(self.app)
        self.map = MapPage(self.app)
        self.data = DataPage(self.app)
        self.about = AboutPage(self.app)
        self.tabs = Tabs(
            [
                TabsList(
                    pos="center",
                    grow=True,
                    children=[
                        TabsTab("Chatbot", value="chatbot"),
                        TabsTab("Dashboard", value="dashboard"),
                        TabsTab("Map", value="map"),
                        TabsTab("Data", value="data"),
                        TabsTab("About", value="about"),
                    ]
                ),
                TabsPanel(self.chatbot.render(), value="chatbot"),
                TabsPanel(self.dashboard.render(), value="dashboard"),
                TabsPanel(self.map.render(), value="map"),
                TabsPanel(self.data.render(), value="data"),
                TabsPanel(self.about.render(), value="about"),
            ]
        )

    def render(self):
        return self.tabs
