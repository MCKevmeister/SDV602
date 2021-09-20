"""
Data Explorer
An example module. Read here about Python documentation: https://ecampus.nmit.ac.nz/moodle/mod/page/view.php?id=1140770

Details about this module.

This module is actually main app.
The main data explorer view is the default View.
It uses controllers for code that runs when GUI actions are happening.

The approach to be taken is to replace the PySimple GUI event loop - the "while" for a Window, with calls to controllers.
Each Controller decides which View to show, each View is linked to Controllers. 
Each controller accepts an input action from the GUI presented or rendered by View.

Thoughts 
This could be an equivalent to a Router ...



"""
import sys
from view.data_explorer_view import DES_View

sys.dont_write_bytecode = True


if __name__ == "__main__":
    """
    Code that runs when this is the main module.
    """
    des_obj = DES_View()
    des_main = des_obj.state_closures()
    des_main['set_up_layout']()
    des_main['render']()
    des_main['accept_input']()

    pass
