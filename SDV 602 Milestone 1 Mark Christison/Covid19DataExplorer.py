import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import datetime
import calendar
import itertools

matplotlib.use('TkAgg')

fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# ------ Menu Definition ------ #
menu_def = [['Account', ['Login', 'Logout', 'Create Account']],
            ['Data Explorer', ['View Current Total Cases', 'View Current Active Cases', 'View Total Deaths']],
            ['Chat', ['Open Chat Window']],
            ['Quit', ['Quit']]]

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
    if event == 'Create Account':
        create_account_window()
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


def login():
    # TODO
    return 0


def logout():
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


def create_account():
    # TODO
    return 0


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def popup_get_date(start_mon=None, start_day=None, start_year=None, begin_at_sunday_plus=0, no_title_bar=True,
                   title='Choose Date', keep_on_top=True, location=(None, None), close_when_chosen=False, icon=None,
                   locale=None, month_names=None, day_abbreviations=None):
    if month_names is not None and len(month_names) != 12:
        sg.popup_error('Incorrect month names list specified. Must have 12 entries.', 'Your list:', month_names)

    if day_abbreviations is not None and len(day_abbreviations) != 7:
        sg.popup_error('Incorrect day abbreviation list. Must have 7 entries.', 'Your list:', day_abbreviations)

    day_font = 'TkFixedFont 9'
    mon_year_font = 'TkFixedFont 10'
    arrow_font = 'TkFixedFont 7'

    now = datetime.datetime.now()
    cur_month, cur_day, cur_year = now.month, now.day, now.year
    cur_month = start_mon or cur_month
    if start_mon is not None:
        cur_day = start_day
    else:
        cur_day = cur_day
    cur_year = start_year or cur_year

    def update_days(window, month, year, begin_at_sunday_plus):
        [window[(week, day)].update('') for day in range(7) for week in range(6)]
        weeks = calendar.monthcalendar(year, month)
        month_days = list(itertools.chain.from_iterable([[0 for _ in range(8 - begin_at_sunday_plus)]] + weeks))
        if month_days[6] == 0:
            month_days = month_days[7:]
            if month_days[6] == 0:
                month_days = month_days[7:]
        for i, day in enumerate(month_days):
            offset = i
            if offset >= 6 * 7:
                break
            window[(offset // 7, offset % 7)].update(str(day) if day else '')

    def make_days_layout():
        days_layout = []
        for week in range(6):
            row = []
            for day in range(7):
                row.append(sg.T('', size=(4, 1), justification='c', font=day_font, key=(week, day), enable_events=True,
                                pad=(0, 0)))
            days_layout.append(row)
        return days_layout

    # Create table of month names and week day abbreviations

    if day_abbreviations is None or len(day_abbreviations) != 7:
        fwday = calendar.SUNDAY
        try:
            if locale is not None:
                _cal = calendar.LocaleTextCalendar(fwday, locale)
            else:
                _cal = calendar.TextCalendar(fwday)
            day_names = _cal.formatweekheader(3).split()
        except Exception as e:
            print('Exception building day names from locale', locale, e)
            day_names = ('Sun', 'Mon', 'Tue', 'Wed', 'Th', 'Fri', 'Sat')
    else:
        day_names = day_abbreviations

    mon_names = month_names if month_names is not None and len(month_names) == 12 else [calendar.month_name[i] for i in
                                                                                        range(1, 13)]
    days_layout = make_days_layout()

    layout = [[sg.B('◄◄', font=arrow_font, border_width=0, key='-YEAR-DOWN-', pad=((10, 2), 2)),
               sg.B('◄', font=arrow_font, border_width=0, key='-MON-DOWN-', pad=(0, 2)),
               sg.Text('{} {}'.format(mon_names[cur_month - 1], cur_year), size=(16, 1), justification='c',
                       font=mon_year_font, key='-MON-YEAR-', pad=(0, 2)),
               sg.B('►', font=arrow_font, border_width=0, key='-MON-UP-', pad=(0, 2)),
               sg.B('►►', font=arrow_font, border_width=0, key='-YEAR-UP-', pad=(2, 2))]]
    layout += [[sg.Col([[sg.T(day_names[i - (7 - begin_at_sunday_plus) % 7], size=(4, 1), font=day_font,
                              background_color=sg.theme_text_color(), text_color=sg.theme_background_color(),
                              pad=(0, 0)) for i in range(7)]], background_color=sg.theme_text_color(), pad=(0, 0))]]
    layout += days_layout
    if not close_when_chosen:
        layout += [[sg.Button('Ok', border_width=0, font='TkFixedFont 8'),
                    sg.Button('Cancel', border_width=0, font='TkFixedFont 8')]]

    window = sg.Window(title, layout, no_titlebar=no_title_bar, grab_anywhere=True, keep_on_top=keep_on_top,
                       font='TkFixedFont 12', use_default_focus=False, location=location, finalize=True, icon=icon)

    update_days(window, cur_month, cur_year, begin_at_sunday_plus)

    prev_choice = chosen_mon_day_year = None

    if cur_day:
        chosen_mon_day_year = cur_month, cur_day, cur_year
        for week in range(6):
            for day in range(7):
                if window[(week, day)].DisplayText == str(cur_day):
                    window[(week, day)].update(background_color=sg.theme_text_color(),
                                               text_color=sg.theme_background_color())
                    prev_choice = (week, day)
                    break

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            chosen_mon_day_year = None
            break
        if event == 'Ok':
            break
        if event in ('-MON-UP-', '-MON-DOWN-', '-YEAR-UP-', '-YEAR-DOWN-'):
            cur_month += (event == '-MON-UP-')
            cur_month -= (event == '-MON-DOWN-')
            cur_year += (event == '-YEAR-UP-')
            cur_year -= (event == '-YEAR-DOWN-')
            if cur_month > 12:
                cur_month = 1
                cur_year += 1
            elif cur_month < 1:
                cur_month = 12
                cur_year -= 1
            window['-MON-YEAR-'].update('{} {}'.format(mon_names[cur_month - 1], cur_year))
            update_days(window, cur_month, cur_year, begin_at_sunday_plus)
            if prev_choice:
                window[prev_choice].update(background_color=sg.theme_background_color(),
                                           text_color=sg.theme_text_color())
        elif type(event) is tuple:
            if window[event].DisplayText != "":
                chosen_mon_day_year = cur_month, int(window[event].DisplayText), cur_year
                if prev_choice:
                    window[prev_choice].update(background_color=sg.theme_background_color(),
                                               text_color=sg.theme_text_color())
                window[event].update(background_color=sg.theme_text_color(), text_color=sg.theme_background_color())
                prev_choice = event
                if close_when_chosen:
                    break
    window.close()
    return chosen_mon_day_year


def current_total_cases_window():
    col1 = [[sg.Canvas(key='-CANVAS-')]]

    col2 = [[sg.Text("Choose a Country"), sg.Listbox(["New Zealand", "Australia", "America"])],
            [sg.Button(button_text="Start Data", size=(15, 1)), sg.Button(button_text="End Data", size=(15, 1))],
            [sg.Button(button_text="Update Graph", size=(15, 1)), sg.Button(button_text="Reset Graph", size=(15, 1))]]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.Text("Current total cases", size=(100, 3), key='-TITLE-', justification='center')],
              [sg.Column(col1), sg.Column(col2, element_justification='center')]]

    window = sg.Window(TITLE + " - Current Total Cases", layout, finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, fig)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == "Start Data":
            popup_get_date()
        if event == "End Data":
            popup_get_date()
        if event in menu_options:
            menu(event, window)
    window.close()


def current_active_cases_window():
    col1 = [[sg.Canvas(key='-CANVAS-')]]

    col2 = [[sg.Text("Choose a Country"), sg.Listbox(["New Zealand", "Australia", "America"])],
            [sg.Button(button_text="Start Data", size=(15, 1)), sg.Button(button_text="End Data", size=(15, 1))],
            [sg.Button(button_text="Update Graph", size=(15, 1)), sg.Button(button_text="Reset Graph", size=(15, 1))]]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.Text("Current Active Cases", size=(100, 3), key='-TITLE-', justification='center')],
              [sg.Column(col1), sg.Column(col2, element_justification='center')]]

    window = sg.Window(TITLE + ' - Current Active Cases', layout, finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, fig)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == "Start Data":
            popup_get_date()
        if event == "End Data":
            popup_get_date()
        if event in menu_options:
            menu(event, window)
    window.close()


def view_total_deaths_window():
    col1 = [[sg.Canvas(key='-CANVAS-')]]

    col2 = [[sg.Text("Choose a Country"), sg.Listbox(["New Zealand", "Australia", "America"])],
            [sg.Button(button_text="Start Data", size=(15, 1)), sg.Button(button_text="End Data", size=(15, 1))],
            [sg.Button(button_text="Update Graph", size=(15, 1)), sg.Button(button_text="Reset Graph", size=(15, 1))]]

    layout = [[sg.Menu(menu_def, tearoff=False)],
              [sg.Text("Current Deaths", size=(100, 3), key='-TITLE-', justification='center')],
              [sg.Column(col1), sg.Column(col2, element_justification='center')]]

    window = sg.Window(TITLE + ' - Current Deaths', layout, finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, fig)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        if event == "Start Data":
            popup_get_date()
        if event == "End Data":
            popup_get_date()
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
              [sg.T('If you do not have an account, please create one to continue'), sg.B('Create Account')]]

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
