import PySimpleGUI as sg


def create_account():
    # TODO
    return 0


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
            sg.popup("User has been created")
            break
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()
