from dash import Dash, Input, Output

class NavbarCallbacks:
    def __init__(self, app):
        self.app = app
        self.register_callbacks()

    def register_callbacks(self):
        @self.app.callback(
            Output("page_content", "children"),  # The content area where the selected page will be rendered
            Input("tabs", "value")  # This will listen for tab changes
        )
        def update_content(selected_tab):
            if selected_tab == "chatbot":
                return self.chatbot.render()  # Render chatbot page
            elif selected_tab == "dashboard":
                return self.dashboard.render()  # Render dashboard page
            elif selected_tab == "map":
                return self.map.render()  # Render map page
            elif selected_tab == "data":
                return self.data.render()  # Render data page
            elif selected_tab == "about":
                return self.about.render()  # Render about page
            return "404: Page Not Found"  # If no tab matches, show 404 message
