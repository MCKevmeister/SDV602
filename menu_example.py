"""
Menu examples
"""


def show_menu(menu_list):
    skip_first_flag = True
    header_line = menu_list[0]  # 0 tuple is the header
    print(header_line)
    for item in menu_list:
        if skip_first_flag:
            skip_first_flag = False
        else:
            print(f'{item[0]} {item[1]}')


def make_valid_numbers(menu_list):
    """
    Make a set of valid numbers from a menu_list
    """
    result = set()
    print("in make valid numbers:")
    first = True
    for a_tuple in menu_list:
        if first:
            first = False
        else:
            result = result | {a_tuple[0]}
    return result


def run_menu(menu_list):
    """
    Display a menu
    """
    valid_numbers = make_valid_numbers(menu_list)  # set of valid numbers1
    not_done = True
    while not_done:
        show_menu(menu_list)
        the_value = get_integer_input()
        if the_value in valid_numbers:
            the_cmd = menu_list[the_value][2]
            not_done = the_cmd(the_value)
        else:
            print(f"Oops! {the_value} is not a valid number")


def get_integer_input():
    """
    Input a number
    """
    test = None
    while True:
        try:
            test = input("Enter a number:")
            result = int(test)
            break
        except ValueError:
            print(f'Oops! {test} was not a number')
    return result


def run_menu_one(a_value):
    menu_one = ["Select a number.", (1, "Menu Burger", test_cmd), (2, "Menu Chips", test_cmd), (3, "Quit", quit_cmd)]
    run_menu(menu_one)
    return True


def run_menu_two(a_value):
    menu_two = ["Select a number.", (1, "different", test_cmd), (2, "menu", test_cmd), (3, "items", quit_cmd)]
    run_menu(menu_two)
    return True


def test_cmd(a_value):
    print(f"A dummy command {a_value}")
    return True  # continue


def quit_cmd(a_value):
    print('Thank you, good-bye!')
    return False  # stop


if __name__ == "__main__":
    # testing code for now
    menu_list = ["Select a number.", (1, "Menu One", run_menu_one), (2, "Menu Two", run_menu_two),
                 (3, "Menu Three", test_cmd), (4, "Quit", quit_cmd)]
    run_menu(menu_list)
