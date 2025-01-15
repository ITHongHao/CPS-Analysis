from dash_mantine_components import Tabs, TabsList, TabsTab, TabsPanel
from Components.chatbot import ChatbotPage
from Components.dashboard import DashboardPage
from Components.data import DataPage
from Components.map import MapPage
from Components.about import AboutPage


# Creates the navigation bar at the top of the website, routes to each of the pages
class Navbar:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        # Initialize all pages
        self.chatbot = ChatbotPage(self.app)
        self.dashboard = DashboardPage(self.app)
        self.map = MapPage(self.app)
        self.data = DataPage(self.app)
        self.about = AboutPage(self.app)
        
        # Set up Tabs component
        self.tabs = Tabs(
            value="chatbot",  # Set the default tab value to "chatbot"
            # style={'height': '60px'},  # Adjust the overall height of the Tabs component
            children=[
                TabsList(
                    pos="center",
                    grow=True,
                    style={'height': '100%'},  # Ensure the list takes up the full height
                    children=[
                        TabsTab("Chatbot", value="chatbot", style={'height': '80px'}),  # Set height for each tab
                        TabsTab("Dashboard", value="dashboard", style={'height': '80px'}),
                        TabsTab("Map", value="map", style={'height': '80px'}),
                        TabsTab("Data", value="data", style={'height': '80px'}),
                        TabsTab("About", value="about", style={'height': '80px'}),
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
