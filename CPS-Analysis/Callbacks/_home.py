from typing import Protocol
from Components.chatbot import ChatbotPage
from dash import Dash, Input, Output
from dash.dcc import Location
from dash.html import Div

class HomeCallbackMembers(Protocol):
    app: Dash
    location: Location
    page_content: Div
    chatbot: ChatbotPage


class HomeCallbacks(HomeCallbackMembers):
    def __init__(self):
        self.register_callbacks()

    def register_callbacks(self):
        @self.app.callback(
            Output(f"{self.location.id}", "pathname"),
            Input(f"{self.location.id}", "pathname"),
            prevent_initial_call=True  # Avoid loops during initialization
        )
        def redirect_to_default(pathname):
            if pathname != "/":
                return "/"
            return pathname

        @self.app.callback(
            Output(f"{self.page_content.id}", "children"),
            Input(f"{self.location.id}", "pathname")
        )
        def handle_page_selection(pathname):
            if pathname == "/":
                return self.chatbot.render()  # Default page
            return Div("404: Page Not Found")

