import dash_mantine_components as dmc
from dash import dcc, html
import folium
from folium import Map
import base64
from io import BytesIO
from dash.dependencies import Input, Output

class MapPage:
    def __init__(self, app):
        self.app = app
        self.gen_components()
        self.register_callbacks()

    def gen_components(self):
        # Generate components for the map page (if needed in the future)
        print("Map Page generated")

    def create_folium_map(self, map_type="Data 1"):
        """
        Generates a Folium map as an HTML string.
        """
        # Initialize the Folium map
        m = Map(location=[37.7749, -122.4194], zoom_start=12)  # Default location: San Francisco

        # Add different data layers based on `map_type`
        if map_type == "Data 1":
            folium.Marker(
                [37.7749, -122.4194], popup="Example Data Point 1", tooltip="San Francisco"
            ).add_to(m)
        elif map_type == "Data 2":
            folium.CircleMarker(
                [37.7799, -122.4294],
                radius=10,
                color="blue",
                fill=True,
                fill_color="blue",
                popup="Example Data Point 2",
            ).add_to(m)

        # Save the Folium map to an HTML string
        map_data = BytesIO()
        m.save(map_data, close_file=False)
        return map_data.getvalue().decode()

    def render(self):
        return dmc.Container([
            dmc.Title("Interactive Map", order=2),
            dmc.Select(
                id="map-type-select",
                label="Choose data to display:",
                data=["Data 1", "Data 2"],
                style={"marginBottom": "20px"}
            ),
            html.Div(
                id="map-container",
                style={"height": "600px", "width": "100%", "border": "1px solid black"}
            )
        ])

    def register_callbacks(self):
        @self.app.callback(
            Output("map-container", "children"),
            Input("map-type-select", "value")
        )
        def update_map(map_type):
            """
            Updates the displayed Folium map based on the selected map type.
            """
            if not map_type:
                map_type = "Data 1"  # Default to Data 1 if no selection
            folium_map_html = self.create_folium_map(map_type)

            # Embed Folium HTML in an iframe
            return html.Iframe(
                srcDoc=folium_map_html,
                style={
                    "height": "600px",
                    "width": "100%",
                    "border": "none"
                }
            )
