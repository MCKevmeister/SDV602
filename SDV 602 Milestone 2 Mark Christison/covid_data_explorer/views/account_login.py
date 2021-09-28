import PySimpleGUI as sg
from account_controller import login


# def login(username, password):
#     # TODO
#     return 0
#
#
# def logout():
#     # TODO
#     return 0


def login_window():
    layout = [[sg.In('Username', key='-USERNAME-')],
              [sg.In('Password', key='-PASSWORD-')],
              [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))]]

    window = sg.Window('Login', layout)

    while True:
        username = "Mark"
        password = "Password"
        event, values = window.read()
        if event == "OK":
            username = values[username]
            login()
            sg.popup("User has logged in")
            break
        if event == "OK" and values['-USERNAME-'] != username and password != values['-PASSWORD-']:
            sg.popup("Incorrect Username or Password")
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()
