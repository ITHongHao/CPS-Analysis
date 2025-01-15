import dash_mantine_components as dmc
from dash.html import Div
from dash.dcc import Location, Store

from Components.navbar import Navbar
from Components.chatbot import ChatbotPage
from Callbacks._home import HomeCallbacks


class HomePage(HomeCallbacks):
    def __init__(self, app):
        self.app = app
        self.gen_components()
        super().__init__()

    def gen_components(self):
        self.chatbot = ChatbotPage(self.app)  # Default landing page
        self.navbar = Navbar(self.app)
        self.page_content = Div(id="page_content")
        self.location = Location(id="url", refresh=False)
        self.store = Store(id="data-store")

    def render(self):
        return Div(
            children=[
                self.location,
                self.store,
                self.navbar.render(),  # Navbar always visible
            ]
        )
