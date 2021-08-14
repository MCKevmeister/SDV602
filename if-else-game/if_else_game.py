import PySimpleGUI as sg

theme = 'Dark Blue 3'


def pattern_1a_window1():
    sg.theme(theme)

    layout = [[sg.Text('Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Welcome to the Game that never ends', layout)

    event, values = window.read()
    window.close()
    res1 = int(values[0])

    if res1 == 1:
        pattern_1a_game_over()
    elif res1 == 2:
        pattern_1a_game_over()
    elif res1 == 3:
        pattern_1a_game_over()
    else:
        pattern_1a_window2()


def pattern_1a_window2():
    sg.theme('Dark Blue 3')

    layout = [[sg.Text('1.No\n2.Yes\n3.Maybe')],
              [sg.InputText()],
              [sg.Submit()]]

    window = sg.Window('Game that never ends', layout)

    event, values = window.read()
    window.close()
    pattern_1a_game_over()


def pattern_1a_game_over():
    sg.theme('Dark Blue 3')

    layout = [[sg.Text('Game Over Replay?\n1.Yes\n2.No')],
              [sg.InputText('1', key='-INPUT-')],
              [sg.Submit()]]

    window = sg.Window('Game Over - Game that never ends', layout)

    event, values = window.read()
    window.close()
    print(values[0])
    res1 = values[0]

    if res1 == 1:
        pattern_1a_window1()
    elif res1 == 2:
        pattern_1a_window1()
    else:
        sg.Popup(event, values, values['-INPUT-'])


def pattern_2b():
    count = 0
    sg.theme('Dark Blue 3')
    question_1 = "Where are you?"
    question_2 = 'What is the answer?'
    text_game_over = "Game Over Replay?"
    layout = [[sg.Text(question_1, key='phrase', size=(20, None))],
              {sg.Button('Nowhere', key='button1'),
               sg.Button('Everywhere', key='button2'),
               sg.Button('Somewhere', key='button3')}]

    window = sg.Window('Window Title', layout, margins=(10, 10), auto_size_text=True, auto_size_buttons=True)

    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED:
            pattern_2b()  # YOU CAN NEVER LEAVE
        if count == 0:
            count = + 1
            window['button1'].update("No")
            window['button2'].update("Yes")
            window['button3'].update("Maybe")
            window['phrase'].update(question_2)
        if count == 1:
            if event == "Yes":
                pattern_2b()
            count = 0
            window['button1'].update("No")
            window['button2'].update("Yes")
            window['button3'].update("Maybe")
            window['phrase'].update(text_game_over)


def game():
    print("Where are you?\n1.Nowhere\n2.Everywhere\n3.Somewhere")
    res1 = int(input())

    if res1 == 1:
        game_over()
    elif res1 == 2:
        game_over()
    elif res1 == 3:
        game_over()
    else:
        print("No, Yes or Maybe")
        res2 = str(input())
        if res2 == "No":
            game_over()
        elif res2 == "Yes":
            game_over()
        elif res2 == "Maybe":
            game_over()
        else:
            game_over()


def game_over():
    print("Game Over\nReplay?\nYes\nNo")
    replay = str(input()).lower()
    if replay == "yes":
        game()
    elif replay == "no":
        print("You can never stop playing")
        game()
    else:
        print("You Won")


if __name__ == "__main__":
    # game()
    # pattern_1a_window1()
    pattern_2b()
