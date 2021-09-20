import PySimpleGUI as sg


def login():
    # TODO
    return 0


def logout():
    # TODO
    return 0


def login_window():
    layout = [[sg.Text('Username')],
              [sg.In(key='-USERNAME-')],
              [sg.Text('Password')],
              [sg.In(key='-PASSWORD-')],
              [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))]]

    window = sg.Window('Login', layout)

    while True:
        username = "Mark"
        password = "Password"
        event, values = window.read()
        if event == "OK" and values['-USERNAME-'] == username and password == values['-PASSWORD-']:
            sg.popup("User has logged in")
            break
        if event == "OK" and values['-USERNAME-'] != username and password != values['-PASSWORD-']:
            sg.popup("Incorrect Username or Password")
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()




