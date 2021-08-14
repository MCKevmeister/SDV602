def fizz_buzz(fizz_on_multiple_of, buzz_on_multiple_of, up_to):
    """
    :param fizz_on_multiple_of: number that produces "Fizz" on its multiples
    :param buzz_on_multiple_of: number that produces "Buzz" on its multiples
    :param up_to: number that is the maximum of the FizzBuzz
    :return: a list of tuples (number, "Fizz/Buzz/Number")
    """
    the_list_of_tuples = []
    i: int = 1
    while i < up_to + 1:
        if i % fizz_on_multiple_of == 0 and i % buzz_on_multiple_of == 0:
            the_list_of_tuples.append(tuple((i, "FizzBuzz")))
        elif i % fizz_on_multiple_of == 0:
            the_list_of_tuples.append(tuple((i, "Fizz")))
        elif i % buzz_on_multiple_of == 0:
            the_list_of_tuples.append(tuple((i, "Buzz")))
        else:
            the_list_of_tuples.append(tuple((i, str(i))))
        i += 1
    return the_list_of_tuples


print(fizz_buzz(3, 5, 15))
