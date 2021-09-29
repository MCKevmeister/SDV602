from account_login import login_window
from create_account import create_account_window
from current_total_cases import current_total_cases_window
from current_active_cases import current_active_cases_window
from total_deaths import view_total_deaths_window
from chat import chat_window
from account_controller import logout
from webbrowser import open

menu_def = [['Account', ['Login', 'Logout', 'Create Account']],
            ['Data Explorer', ['View Current Total Cases',
                               'View Current Active Cases',
                               'View Total Deaths',
                               'Source Data Link']],
            ['Chat', ['Open Chat Window']],
            ['Quit', ['Quit']]]

menu_options = ['Login', 'Logout', 'Create Account',
                'View Current Total Cases', 'View Current Active Cases', 'View Total Deaths',
                'Open Chat Window',
                'Quit']

TITLE = "Covid-19 Data Explorer"


def run_menu(event, window):
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
    if event == 'Source Data Link':
        open(r'https://github.com/owid/covid-19-data/blob/master/public/data/README.md')
    if event == 'Open Chat Window':
        window.close()
        chat_window()
    if event == 'Quit':
        window.close()
