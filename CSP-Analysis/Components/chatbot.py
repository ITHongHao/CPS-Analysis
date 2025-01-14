import dash_mantine_components as dmc


# displays all information and statistical tests
class ChatbotPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        print("Chatbot Page Generated")

    def render(self):
        return dmc.Stack([
            dmc.Text("Chatbot Page"),
        ])
