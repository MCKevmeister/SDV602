import PySimpleGUI as sg 

def pattern_1a():
    """
    Pattern 1 A - "One-shot Window"
    Read a window one time then close it
    """
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                    [sg.InputText(), sg.FileBrowse()],
                    [sg.Submit(), sg.Cancel()]]

    window = sg.Window('SHA-1 & 256 Hash', layout)

    event, values = window.read()
    window.close()

    source_filename = values[0]     # the first input element is values[0]
    return source_filename

def pattern_1b():
    """
    Pattern 1 B - "One-shot Window" - 
    Read a window one time then close it (compact format)
    """
    sg.theme('Dark Blue 3')  # please make your windows colorful

    event, values  = sg.Window('SHA-1 & 256 Hash', [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                            [sg.InputText(), sg.FileBrowse()],
                            [sg.Submit(), sg.Cancel()]]).read(close=True)

    source_filename = values[0]     # the first input element is values[0]
    
    return source_filename

def pattern_2a():
    """
    Pattern 2 A - Persistent window 
    (multiple reads using an event loop)
    """
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Persistent window')],
            [sg.Input()],
            [sg.Button('Read'), sg.Exit()]]

    window = sg.Window('Window that stays open', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        print(event, values)

    window.close()

def pattern_2b():
    """
    Pattern 2 B - Persistent window 
    (multiple reads using an event loop + updates data in window)
    """
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
            [sg.Input(key='-IN-')],
            [sg.Button('Show'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout)

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Show':
            # change the "output" element to be the value of "input" element
            window['-OUTPUT-'].update(values['-IN-'])

    window.close()

def return_values():
    
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Rename files or folders')],
        [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
        [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel()]]

    window = sg.Window('Rename Files or Folders', layout)

    event, values = window.read()
    window.close()
    folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
    print(folder_path, file_path)

def return_values_dictionary() : # key spec in the layout
    """
    Get values returned from the window with keys
     so you can look them up using a dictionary
    """
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [
                [sg.Text('Please enter your Name, Address, Phone')],
                [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='-NAME-')],
                [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='-ADDRESS-')],
                [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='-PHONE-')],
                [sg.Submit(), sg.Cancel()]
                ]

    window = sg.Window('Simple data entry window', layout)
    event, values = window.read()
    window.close()

    sg.Popup(event, values, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])

def confirm_with_pop():
    """
    Confirm exit with sg.popup yes/no
    """

    layout = [[sg.Text('Very basic Window')],
            [sg.Text('Click X in titlebar or the Exit button')],
            [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, enable_close_attempted_event=True)

    while True:
        event, values = window.read()
        print(event, values)
        if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
            break

    window.close()

if __name__ == "__main__" :
    #testing for now
    print(f'Pattern 1a {pattern_1a()} Pattern 1b {pattern_1b} \n')
    pattern_2a()
    pattern_2b()
    return_values()
    return_values_dictionary()
    confirm_with_pop()
    pass