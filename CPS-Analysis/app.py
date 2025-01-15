import dash
import dash_mantine_components as dmc
from Components.home import HomePage

def create_app():
    """
    Factory function to create and configure the Dash app.
    """
    app = dash.Dash(
        __name__,
        suppress_callback_exceptions=True,  # Allows dynamic layouts and callbacks
        title="CPSBot",  # Sets the browser tab title
        update_title="Loading...",  # Sets the title shown during app updates
        meta_tags=[  # Adds responsive design meta tag
            {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
        ],
    )

    # Set the layout inside MantineProvider for theming
    app.layout = dmc.MantineProvider(
        theme={
            "colorScheme": "dark",  # Enable dark mode
            "primaryColor": "teal",  # Primary color for buttons, accents, etc.
            "fontFamily": "Verdana, sans-serif",  # Choose a font
            "defaultRadius": 8,  # Radius for rounded corners
            "spacing": {"xs": 4, "sm": 10, "md": 20},
        },
        children=[HomePage(app).render()]  # Make sure this is wrapped inside MantineProvider
    )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run_server(debug=True)
