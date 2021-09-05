"""
Presents an example based on Demo_Matplotlib_Browser
"""
import inspect
import PySimpleGUI as sg
import matplotlib
import ChartExamples as ce
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('TkAgg')


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')


def embedded_plt(fig_dict):
    sg.theme("LightGreen")

    figure_w, figure_h = 650, 650
    # define the form layout
    listbox_values = list(fig_dict)
    col_listbox = [
        [sg.Listbox(values=listbox_values, enable_events=True, size=(28, len(listbox_values)), key='-LISTBOX-')],
        [sg.Text(' ' * 12), sg.Exit(size=(5, 2))]]

    layout = [[sg.Text('Matplotlib Plot Test', font='current 18')],
              [sg.Col(col_listbox, pad=(5, (3, 330))), sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-'),
               sg.MLine(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')], ]

    # create the form and show it without the plot
    window = sg.Window('Our Demo Application - Embedding Matplotlib In PySimpleGUI with **kwargs', layout,
                       grab_anywhere=False, finalize=True)
    figure_agg = None
    # The GUI Event Loop
    while True:
        event, values = window.read()
        # print(event, values)
        # helps greatly when debugging
        if event in (sg.WIN_CLOSED, 'Exit'):  # if user closed window or clicked Exit button
            break
        if figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            delete_figure_agg(figure_agg)
        choice = values['-LISTBOX-'][0]  # get first listbox item chosen (returned as a list)
        func_tuple = fig_dict[choice]  # get function to call from the dictionary
        kwargs = func_tuple[1]
        func = func_tuple[0]
        window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline

        fig = func(**kwargs)  # call function to get the figure
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)  # draw the figure
    window.close()


if __name__ == "__main__":
    # ce.show_figFunc(ce.bar_chart)

    dictionary_of_figure_functions = {'Line Plot': (ce.line_plot, {'plot': [1, 4.5, 1, 23]}),
                                      'Plot Dots(discrete plot)': (ce.discrete_plot, {'plot': [1, 4.5, 1, 23],
                                                                                      'fmt': 'ob'}),
                                      'Name and Label': (ce.names_labels, {'xlabel': 'Days',
                                                                           'ylabel': 'Temperature in Celsius',
                                                                           'title': 'Temperature Graph'}),
                                      'Plot many Lines': (ce.multiple_plots, {'xlabel': 'Day',
                                                                              'ylabel': 'Temperature in Celsius',
                                                                              'title': 'Temperature Graph'}),
                                      'Bar Chart': (ce.bar_chart, {'visitors': [1241, 50927, 162242, 222093, 665004,
                                                                                2071987, 2460407, 3799215, 5399000,
                                                                                5474016, 6003672],
                                                                   'color': 'green',
                                                                   'xlabel': 'Years',
                                                                   'ylabel': "Values",
                                                                   'title': "Bar Chart Example"}),
                                      'Histogram': (ce.histogram, {'title': 'Our Histogram Name',
                                                                   'gaussian_numbers': np.random.normal(size=10000),
                                                                   'bins': 20
                                                                   }),
                                      'Scatter Plots': (ce.scatter_plots, {'x': np.arange(0, 11),
                                                                           'y1': np.random.randint(2, 7, (11,)),
                                                                           'y2': np.random.randint(9, 14, (11,)),
                                                                           'y3': np.random.randint(15, 25, (11,)),
                                                                           'title': 'Scatter Plot Example'}),
                                      'Stack Plot': (ce.stack_plot, {'idxes': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                     'y1': [23, 42, 33, 43, 8, 44, 43, 18, 21],
                                                                     'y2': [9, 31, 25, 14, 17, 17, 42, 22, 28],
                                                                     'y3': [18, 29, 19, 22, 18, 16, 13, 32, 21],
                                                                     'title': 'Stack Plot Example'}),
                                      'Pie Chart 1': (ce.pie_chart1, {}),
                                      'Pie Chart 2': (ce.pie_chart2, {})}
    embedded_plt(dictionary_of_figure_functions)
