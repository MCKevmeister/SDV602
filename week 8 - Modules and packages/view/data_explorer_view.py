import sys
sys.dont_write_bytecode = True
from typing import Dict
import view.ChartExamples as ce 
import controller.DES.exit_button as exit_button
import controller.DES.figure_list_select as figure_list_select
import controller.DES.new_des as new_des
import PySimpleGUI as sg
import inspect
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import matplotlib.pyplot as plt

class DES_View(object):
    des_list = []
    current_des = 0
    def __init__(self):
        
        self.window = None
        self.figure_agg = None
        self.layout = []
        self.components = {"has_components":False}
        self.controls = []
        self.my_lastfig = None
        self.fig_dict = {'Line Plot':(ce.line_plot,{}),'Plot Dots(discrete plot)':(ce.discrete_plot,{}),
    'Name and Label':(ce.names_labels,{}),'Plot many Lines':(ce.multiple_plots,{}),
    'Bar Chart':(ce.bar_chart,{}),'Histogram':(ce.histogram,{'title':'Our Histogram Name'}),
    'Scatter Plots':(ce.scatter_plots,{}),'Stack Plot':(ce.stack_plot,{}),
    'Pie Chart 1':(ce.pie_chart1,{}),
    'Pie Chart 2':(ce.pie_chart2,{})}
        DES_View.current_des +=1 
        DES_View.des_list += [self]


    def state_closures(self):    
        def draw_figure(canvas, figure):
            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
            return figure_canvas_agg

        def delete_figure_agg(figure_agg):
            
            if self.figure_agg:
                self.figure_agg.get_tk_widget().forget()
            plt.close('all')


        def figure_list_draw(values):
            

            choice = values['-LISTBOX-'][0]                 # get first listbox item chosen (returned as a list)
            func_tuple = self.fig_dict[choice]                         # get function to call from the dictionary
            kwargs = func_tuple[1]
            
            func = func_tuple[0]
            
            
            self.window['-MULTILINE-'].update(inspect.getsource(func))  # show source code to function in multiline
             
            fig = func(**kwargs)                                    # call function to get the figure
            
            # ** IMPORTANT ** Clean up previous drawing before drawing again
            delete_figure_agg(self.figure_agg)

            self.figure_agg = draw_figure(self.window['-CANVAS-'].TKCanvas, fig)  # draw the figure
        



        def set_up_layout(**kwargs):

            sg.theme('LightGreen')
            figure_w, figure_h = 650, 650
            # define the form layout
            listbox_values = list(self.fig_dict)
            print(f"GOT List box {listbox_values}")
            # one variable per call to sg 
            # if there is a control / input with it add the name to the controls list
            self.components['figures_list'] =  sg.Listbox(values=listbox_values, enable_events=True, size=(28, len(listbox_values)), key='-LISTBOX-')
            self.controls += [figure_list_select.accept]

            self.components['text_spacer'] = sg.Text(' ' * 12)
            self.components['new_des'] = sg.Button(button_text="New DES",size=(10, 2))
            self.controls += [new_des.accept]

            self.components['exit_button'] = sg.Exit(size=(5, 2))        
            self.controls += [exit_button.accept]

            col_listbox = [
                            [self.components['figures_list']],
                            [self.components['text_spacer'],self.components['new_des'],self.components['exit_button'] ]
                        ]
            self.components['header'] =   sg.Text('Matplotlib Plot Test', font=('current 18'))
            self.components['list_box_padding'] =  sg.Col(col_listbox, pad=(5, (3, 330))) 
            self.components['canvas']   =   sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-') 
            self.components['MLine']    =  sg.MLine(size=(70, 35), pad=(5, (3, 90)), key='-MULTILINE-')   
            self.layout = [
                    [self.components['header']],
                    [self.components['list_box_padding'],self.components['canvas'],
                    self.components['MLine']]
                    ]

        def render():

            # create the form and show it without the plot
            if self.layout != [] :
                self.window =sg.Window('Our Demo Application - Embedding Matplotlib In PySimpleGUI with **kwargs', self.layout, grab_anywhere=False, finalize=True)
                

        def accept_input():

                if self.window != None :
                    keep_going = True
                    
                    while keep_going == True:
                        event, values = self.window.read()
                        for accept_control in self.controls:
                            keep_going = accept_control(event,values,{'figure_list_draw':figure_list_draw,'self':self})
                    self.window.close()

        return {'set_up_layout':set_up_layout,'render':render,'accept_input':accept_input,'figure_list_draw':figure_list_draw,'current_window':self.window}

