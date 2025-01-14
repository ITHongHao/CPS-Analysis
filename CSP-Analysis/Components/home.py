import dash_mantine_components as dmc
from Components.navbar import Navbar
from Components.chatbot import ChatbotPage


# 
class HomePage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        self.chatbot = ChatbotPage(self.app)        # need to find out how to make this the default landing page
        self.navbar = Navbar(self.app)


    def render(self):
        return dmc.Stack([
            self.navbar.render(),
        ])
