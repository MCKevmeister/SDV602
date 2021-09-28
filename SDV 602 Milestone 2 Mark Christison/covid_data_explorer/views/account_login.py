import PySimpleGUI as sg
from account_controller import login


def login_window():
    layout = [[sg.In('Username', key='-USERNAME-')],
              [sg.In('Password', key='-PASSWORD-')],
              [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))]]

    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()
        if event == "OK":
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if username == "" or password == "":
                sg.popup("Please enter a username and password")
            else:
                login(username, password)
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()
