import dash_mantine_components as dmc
from dash import html, dcc


# displays all information and statistical tests
class ChatbotPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Chatbot Page Generated")

    def render(self):
        return dmc.Container([
            dmc.Title("Chatbot", order=2),
            dcc.Textarea(
                id="chat-input",
                placeholder="Type your message here...",
                style={"width": "100%", "height": "80px", "marginTop": "10px"}
            ),
            dmc.Button("Send", id="send-btn", style={"marginTop": "10px"}),
            html.Div(id="chat-output", style={"marginTop": "20px", "padding": "10px", "border": "1px solid gray"})
        ])
