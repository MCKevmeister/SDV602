import PySimpleGUI as sg
from account_controller import create_account


def create_account_window():
    layout = [[sg.Text('Register your details')],
              [sg.Text('Username')],
              [sg.In(key='-USERNAME-')],
              [sg.Text('Password')],
              [sg.In(key='-PASSWORD-')],
              [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))]]

    window = sg.Window('Create Account', layout)

    while True:
        event, values = window.read()
        if event == "OK":
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            register_message = create_account(username, password)
            sg.popup(register_message)
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()
