import dash_mantine_components as dmc
import random

class Summary:
    def __init__(self, app):
        self.app = app
        self.gen_components()

    def gen_components(self):
        # Create a dummy line chart for the attendance data
        self.chart = dmc.LineChart(
            data=[
                {"date": "2023-01-01", "attendance_rate": random.randint(80, 100)},
                {"date": "2023-01-02", "attendance_rate": random.randint(80, 100)},
                {"date": "2023-01-03", "attendance_rate": random.randint(80, 100)},
            ],
            series=[{"name": "Attendance Rate", "dataKey": "attendance_rate"}],  # Adding the 'series' argument
            dataKey="attendance_rate",  # Keeping dataKey to refer to the specific data series
            lineProps={"stroke": "#0A74DA"},
            w=600,
            h=300,
        )

    def render(self):
        return dmc.Stack([
            dmc.Text("Attendance Summary"), 
            self.chart
        ])
