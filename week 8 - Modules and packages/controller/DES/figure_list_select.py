"""
figure list controller
"""
import sys

sys.dont_write_bytecode = True


def accept(event, values, state):
    figure_list_draw = state['figure_list_draw']
    figure_list_draw(values)
    return True
