import PySimpleGUI as sg


def login_window():
    layout = [
        [sg.Text('Username')],
        [sg.In(key='-USERNAME-')],
        [sg.Text('Password')],
        [sg.In(key='-PASSWORD-')],
        [sg.Button("OK", size=(10, 1)), sg.B("Cancel", size=(10, 1))],
    ]

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
        if event == "Cancel":
            break
    window.close()


def current_total_cases_window():
    return 0


def current_active_cases_window():
    return 0


def chat_window():
    return 0


def settings_window():
    return 0


def program():
    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(1, 1))

    # ------ Menu Definition ------ #
    menu_def = [
        ['Login', ['Login'], ['Logout']],
        ['Data Explorer', ['View Current Total Cases', 'View Current Active Cases', 'View Total Deaths']],
        ['Chat', ['Open Chat Window']],
        ['Settings', ['Open Settings']],
    ]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.T("Welcome to the Covid-19 Data Explorer", size=(100, 30))]]

    window = sg.Window('Covid-19 Data Explorer', layout)

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        print('Button = ', event)

        if event == 'Login':
            login_window()
        if event == 'View Current Total Cases':
            current_total_cases_window()
        if event == 'View Current Active Cases':
            current_active_cases_window()
        if event == 'Open Chat Window':
            chat_window()
        if event == 'Open Settings':
            settings_window()
    window.close()


if __name__ == '__main__':
    program()
