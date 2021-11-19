import PySimpleGUI as sg
import data_plotter
import menu
import elements.popup_calendar as popup_calendar
from elements.draw_figure import draw_figure, get_fig
from local_data import merge_data
from shared_data import data_source, countries


def view_total_deaths_window():
    col1 = [[sg.Canvas(key='-CANVAS-')]]

    col2 = [[sg.Text("Choose a Country"), sg.Combo(values=countries, enable_events=True, key='Country')],
            [sg.Button(button_text="Start Data", size=(15, 1)), sg.Button(button_text="End Data", size=(15, 1))],
            [sg.Text("Merge CSV"), sg.FileBrowse('Merge')],
            [sg.Button(button_text="Update Graph", size=(15, 1)), sg.Button(button_text="Reset Graph", size=(15, 1))]]

    layout = [[sg.Menu(menu.menu_def, tearoff=False)],
              [sg.Text("Current Deaths", size=(100, 3), key='-TITLE-', justification='center')],
              [sg.Column(col1), sg.Column(col2, element_justification='center')]]

    window = sg.Window(menu.TITLE + ' - Current Deaths', layout, finalize=True)

    start_date = None
    end_date = None
    country = None

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == "Start Data":
            start_date = popup_calendar.popup_get_date()
        if event == "End Data":
            end_date = popup_calendar.popup_get_date()
        if event == "Country":
            country = values['Country']
        if event == "Update Graph":
            if (country is not None) and (start_date is not None) and (end_date is not None):
                x, y = data_plotter.filter_data(start_date, end_date, country, 'total deaths', data_source)
                fig = get_fig(x, y)
                draw_figure(window['-CANVAS-'].TKCanvas, fig)
        if event in menu.menu_options:
            menu.run_menu(event, window)
        if event == 'Merge':
            merge_data(values['Merge'])
    window.close()
