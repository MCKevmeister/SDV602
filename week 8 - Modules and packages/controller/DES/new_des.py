"""
New DES button controller
"""
import sys
import view.data_explorer_view as des_view

sys.dont_write_bytecode = True


def accept(event, values, state):
    keep_going = True
    if event == 'New DES':
        des_obj = des_view.DES_View()
        des_main = des_obj.state_closures()
        des_main['set_up_layout']()
        des_main['render']()
        des_main['accept_input']()
    return keep_going
