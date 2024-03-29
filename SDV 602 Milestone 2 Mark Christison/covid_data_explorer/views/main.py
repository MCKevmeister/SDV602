import PySimpleGUI as sg
import menu


def main_view():
    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(1, 1))

    layout = [[sg.Menu(menu.menu_def, tearoff=False)],
              [sg.T("Welcome to the Covid-19 Data Explorer", size=(100, 3), key='-TITLE-')],
              [sg.T('To chat, please login to continue.'), sg.B('Login')],
              [sg.T('If you do not have an account, please create one to continue'), sg.B('Create Account')],
              [sg.T('Choose a data source to view'), sg.B('Local data'), sg.B('Remote data')]]

    window = sg.Window(menu.TITLE, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event in menu.menu_options:
            menu.run_menu(event, window)
    window.close()
