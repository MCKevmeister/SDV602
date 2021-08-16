import PySimpleGUI as sg


def game():
    sg.theme('Dark Blue')
    count = 0

    layout = [[sg.Text(text='Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere', key='-QUESTION-')],
              [sg.Button(button_text='Nowhere', key='-BUTTON1-'),
               sg.Button(button_text='Everywhere', key='-BUTTON2-'),
               sg.Button(button_text='Somewhere', key='-BUTTON3-')]]

    window = sg.Window('Welcome to the game that never ends', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'End':
            break
        elif count == 0 and event != 'End':
            count = + 1
            window['-QUESTION-'].update('What is the answer?\n1.No\n2.Yes\n3.Maybe')
            window['-BUTTON1-'].update('No')
            window['-BUTTON2-'].update('Yes')
            window['-BUTTON3-'].update('Maybe')
        elif count == 1 and event != 'End':
            count = + 1
            window['-QUESTION-'].update('Game Over Replay?\n1.Yes\n2.No\n3.Maybe')
            window['-BUTTON1-'].update('Yes')
            window['-BUTTON2-'].update('No')
            window['-BUTTON3-'].update('Maybe')
        elif count >= 2 and event != 'End':
            count = - 2
            window['-QUESTION-'].update('Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere')
            window['-BUTTON1-'].update('Nowhere')
            window['-BUTTON2-'].update('Everywhere')
            window['-BUTTON3-'].update('Somewhere')
    window.close()


if __name__ == "__main__":
    game()
