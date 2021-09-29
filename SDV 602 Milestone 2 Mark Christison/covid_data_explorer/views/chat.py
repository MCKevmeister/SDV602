import PySimpleGUI as sg
import menu
from chat_controller import send_message, get_messages


def chat_window():
    layout = [[sg.Menu(menu.menu_def, tearoff=False)],
              [sg.T('Welcome to the Covid19 data explorer chat.')],
              [sg.Output(size=(100, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=False, key='-CHAT-', do_not_clear=False),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True)]]

    window = sg.Window(menu.TITLE + ' - Chat window', layout)

    while True:
        event, value = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):
            break
        if event == 'SEND':
            message = value['-CHAT-'].rstrip()
            send_message(message)
        if event in menu.menu_options:
            menu.run_menu(event, window)
        # get_messages()
        # TODO: use observer pattern to get messages when they have been updated in the database
