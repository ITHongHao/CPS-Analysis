from dash.dependencies import Input, Output

# Example callback function that updates a component
def register_callbacks(app):
    @app.callback(
        Output("output_component", "children"), 
        [Input("input_component", "value")]
    )
    def update_output(value):
        return f"You entered: {value}"
