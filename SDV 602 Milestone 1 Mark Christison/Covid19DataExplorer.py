import PySimpleGUI as sg

# ------ Menu Definition ------ #
menu_def = [
    ['Account', ['Login', 'Logout', 'Create Account']],
    ['Data Explorer', ['View Current Total Cases', 'View Current Active Cases', 'View Total Deaths']],
    ['Chat', ['Open Chat Window']],
    ['Quit', ['Quit']]
]

menu_options = ['Login', 'Logout', 'Create Account',
                'View Current Total Cases', 'View Current Active Cases', 'View Total Deaths',
                'Open Chat Window',
                'Quit']

TITLE = "Covid-19 Data Explorer"


def menu(event, window):
    if event == 'Login':
        login_window()
    if event == 'Logout':
        logout()
    if event == 'View Current Total Cases':
        window.close()
        current_total_cases_window()
    if event == 'View Current Active Cases':
        window.close()
        current_active_cases_window()
    if event == 'View Total Deaths':
        window.close()
        view_total_deaths_window()
    if event == 'Open Chat Window':
        window.close()
        chat_window()
    if event == 'Quit':
        window.close()


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


def login():
    # TODO
    return 0


def logout():
    # TODO
    return 0


def create_account():
    # TODO
    return 0


def current_total_cases_window():
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.T("Current total cases", size=(100, 3), key='-TITLE-')],
              [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0, 0), graph_top_right=(400, 400),
                        background_color='grey', enable_events=True, key='graph')],
              [sg.Text('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]]

    window = sg.Window(TITLE + " - Current Total Cases", layout, finalize=True)

    graph = window['graph']
    circle = graph.draw_circle((75, 75), 25, fill_color='black', line_color='white')
    point = graph.draw_point((75, 75), 10, color='green')
    oval = graph.draw_oval((25, 300), (100, 280), fill_color='purple', line_color='purple')
    rectangle = graph.draw_rectangle((25, 300), (100, 280), line_color='purple')
    line = graph.draw_line((0, 0), (100, 100))
    arc = graph.draw_arc((0, 0), (400, 400), 160, 10, style='arc', arc_color='blue')
    poly = graph.draw_polygon(((10, 10), (20, 0), (40, 200), (10, 10)), fill_color='green')
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event in ('Blue', 'Red'):
            graph.TKCanvas.itemconfig(circle, fill=event)
        if event == 'Move':
            graph.MoveFigure(point, 10, 10)
            graph.MoveFigure(circle, 10, 10)
            graph.MoveFigure(oval, 10, 10)
            graph.MoveFigure(rectangle, 10, 10)
            graph.MoveFigure(arc, 10, 10)
            graph.MoveFigure(poly, 10, 10)

        if event in menu_options:
            menu(event, window)
    window.close()


def current_active_cases_window():
    layout = [
        [sg.Menu(menu_def, tearoff=False)],
        [sg.T("Current Active Cases", size=(100, 3), key='-TITLE-')]
    ]

    window = sg.Window(TITLE + ' - Current Active Cases', layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event in menu_options:
            menu(event, window)
    window.close()


def view_total_deaths_window():
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.T("Welcome to the Covid-19 Data Explorer", size=(100, 3), key='-TITLE-')]]

    window = sg.Window(TITLE + ' - Current Deaths', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event in menu_options:
            menu(event, window)
    window.close()


def chat_window():
    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.T('Welcome to the Covid19 data explorer chat.')],
              [sg.Output(size=(100, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=False, key='-CHAT-', do_not_clear=False),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)]]

    window = sg.Window(TITLE + ' - Chat window', layout)

    while True:  # The Event Loop
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):
            break
        if event == 'SEND':
            query = value['-CHAT-'].rstrip()
            print(f'{query}', flush=True)
        if event in menu_options:
            menu(event, window)
    covid_data_explorer()


def covid_data_explorer():
    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(1, 1))

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.T("Welcome to the Covid-19 Data Explorer", size=(100, 3), key='-TITLE-')],
              [sg.T('To view data, please login to continue.'), sg.B('Login')],
              [sg.T('If you do not have an account, please create one to continue'), sg.B('Create Account')],
              ]

    window = sg.Window(TITLE, layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event in menu_options:
            menu(event, window)
    window.close()


if __name__ == '__main__':
    covid_data_explorer()
