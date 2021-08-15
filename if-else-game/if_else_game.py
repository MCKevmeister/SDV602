import PySimpleGUI as sg


def game():
    sg.theme('Dark Blue')
    count = 0

    layout = [[sg.T(text='Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere', key='-Q-', size=(50, 1))],
              [sg.B(key='-B1-'),
               sg.B(key='-B2-'),
               sg.B(button_text='Somewhere', key='-B3-')]]

    window = sg.Window('Welcome to the game that never ends', layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'End':
            break
        elif count == 0 and event != 'End':
            count = + 1
            window['-Q-']('What is the answer?\n1.No\n2.Yes\n3.Maybe')
            window['-B1-']('No')
            window['-B2-']('Yes')
            window['-B3-']('Maybe')
        elif count == 1 and event != 'End':
            count = -1
            window['-Q-']('Game Over Replay?\n1.Yes\n2.No\n3.Maybe')
            window['-B1-']('Yes')
            window['-B2-']('No')
            window['-B3-']('Maybe')
        elif count == -1 and event != 'End':
            count = 0
            window['-Q-']('Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere')
            window['-B1-']('Nowhere')
            window['-B2-']('Everywhere')
            window['-B3-']('Somewhere')

    window.close()


if __name__ == "__main__":
    game()
