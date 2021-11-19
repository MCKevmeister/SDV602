import PySimpleGUI as sg
from local_data import validate_csv_format, merge_data


def local_csv_upload_window():
    layout = [
        [sg.Input(), sg.FileBrowse('FileBrowse')],
        [sg.B("Ok", key='Ok'), sg.Cancel()],
    ]

    window = sg.Window('Upload Local CSV', layout)

    while True:
        event, values = window.read()

        if event is None or event == 'Cancel':
            break

        if event == 'Ok':
            print('FileBrowse:', values['FileBrowse'])
            if validate_csv_format(values['FileBrowse']):
                merge_data(values['FileBrowse'])
    window.close()
