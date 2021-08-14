import PySimpleGUI as sg


def game():
    sg.theme('Dark Blue')
    answer_count = 0

    layout = [[sg.Text(text='Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere', key='-QUESTION-')],
              [sg.Button(button_text='Nowhere', key='-BUTTON1-'),
               sg.Button(button_text='Everywhere', key='-BUTTON2-'),
               sg.Button(button_text='Somewhere', key='-BUTTON3-')]]

    window = sg.Window('Welcome to the game that never ends', layout)

    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'End':
            break
        elif answer_count == 0 and event != 'End':
            answer_count = + 1
            input.update
            window['-QUESTION-'].update(text='What is the answer?\n1.No\n2.Yes\n3.Maybe')
            # doesnt update the text value?? No idea why

            window['-BUTTON1-'].update(button_text='No')
            window['-BUTTON2-'].update(button_text='Yes')
            window['-BUTTON3-'].update(button_text='Maybe')
        elif answer_count == 1 and event != 'End':
            answer_count = + 1
            window['-QUESTION-'].update(text='Game Over Replay?\n1.Yes\n2.No\n3.Maybe')
            window['-BUTTON1-'].update(button_text='Yes')
            window['-BUTTON2-'].update(button_text='No')
            window['-BUTTON3-'].update(button_text='Maybe')
        elif answer_count == 2 and event != 'End':
            answer_count = 0
            window['-QUESTION-'].update(text='Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere')
            window['-BUTTON1-'].update(button_text='Nowhere')
            window['-BUTTON2-'].update(button_text='Everywhere')
            window['-BUTTON3-'].update(button_text='Somewhere')
    window.close()


if __name__ == "__main__":
    game()
