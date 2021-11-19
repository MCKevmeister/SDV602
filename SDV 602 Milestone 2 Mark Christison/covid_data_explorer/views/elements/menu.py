import webbrowser
from account_login import login_window
from chat import chat_window
from create_account import create_account_window
from current_total_cases import current_total_cases_window
from get_remote_data import get_df
from total_deaths import view_total_deaths_window
from total_vaccinations import total_vaccinations_window
import user_manager
from local_csv_upload import local_csv_upload_window

menu_def = [['Account', ['Login', 'Logout', 'Create Account']],
            ['Data Explorer', ['Data', ['Local CSV', 'Online CSV'],
                               'View Current Total Cases',
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
    """
    Handles events triggered from the menu bar

    :param event: Event that is triggered
    :type event: string
    :param window: Window that triggers the menu event
    :type window: window
    """
    if event == 'Login':
        login_window()
    if event == 'Logout':
        user = user_manager.UserManager()
        user.logout()
    if event == 'Create Account':
        create_account_window()
    if event == 'Local CSV':
        window.close()
        local_csv_upload_window()
    if event == 'Online CSV':
        get_df()
    if event == 'View Current Total Cases':
        window.close()
        current_total_cases_window()
    if event == 'View Current Active Cases':
        window.close()
        total_vaccinations_window()
    if event == 'View Total Deaths':
        window.close()
        view_total_deaths_window()
    if event == 'Source Data Link':
        webbrowser.open(r'https://github.com/owid/covid-19-data/blob/master/public/data/README.md', 1)
    if event == 'Open Chat Window':
        window.close()
        chat_window()
    if event == 'Quit':
        window.close()
