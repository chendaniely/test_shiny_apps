import pandas as pd
from shiny import App, render, reactive, ui

from shiny_adaptive_filter import adaptive_filter_module

data = {
    "total_bill": [16.99, 10.34, 21.01, 23.68, 24.59],
    "tip": [1.01, 1.66, 3.50, 3.31, 3.61],
    "sex": ["Female", "Male", "Male", "Male", "Female"],
    "smoker": ["No", "No", "No", "No", "Yes"],
    "day": ["Sun", "Sun", "Sun", "Fri", "Sun"],
    "time": ["Lunch", "Dinner", "Dinner", "Dinner", "Dinner"],
    "size": [2, 3, 3, 2, 4],
}

tips = pd.DataFrame(data)

app_ui = ui.page_sidebar(
    ui.sidebar(
        adaptive_filter_module.filter_ui("adaptive"),  # <<
    ),
    ui.output_data_frame("render_df"),
)


def server(input, output, session):
    @reactive.calc  # <<
    def tips_reactive():  # <<
        return tips  # <<

    @reactive.calc
    def data_filtered():
        df = tips_reactive().loc[filter_idx()]  # <<
        return df

    @render.data_frame
    def render_df():
        return render.DataGrid(data_filtered())

    filter_return = adaptive_filter_module.filter_server(  # <<
        "adaptive",  # <<
        df=tips_reactive,  # <<
    )  # <<
    filter_idx = filter_return["filter_idx"]  # <<


app = App(app_ui, server)
