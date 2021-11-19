import PySimpleGUI as sg
import user_manager


def login_window():
    layout = [[sg.Text("Username")], [sg.In('', key='-USERNAME-')],
              [sg.Text("Password")], [sg.In('', key='-PASSWORD-')],
              [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))]]

    window = sg.Window('Login', layout)

    while True:
        event, values = window.read()
        if event == "OK":
            username = values['-USERNAME-']
            password = values['-PASSWORD-']
            if username == "" or password == "":
                sg.popup("Please enter a username and password")
                login_window()
            else:
                user = user_manager.UserManager()
                user.login(username, password)
        if event == sg.WIN_CLOSED or "Cancel":
            break
    window.close()
