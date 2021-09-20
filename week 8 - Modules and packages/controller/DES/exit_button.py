"""
Exit button controller
"""
import sys
import PySimpleGUI as sg

sys.dont_write_bytecode = True


def accept(event, values, state):
    if event in (sg.WIN_CLOSED, 'Exit'):
        keep_going = False
    else:
        keep_going = True

    return keep_going
