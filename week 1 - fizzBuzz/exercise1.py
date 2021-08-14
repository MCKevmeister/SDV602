def fizzBuzz(up_to_number):
    """
    Exercise 1
    Define a procedure that starts at zero and writes the correct “FizzBuzz” on a separate line,
    for each in the sequence up to a number. Use the for control statement, i.e. “for i in range( up_to_number )”.
    Pass the number you are going “up to” as a parameter to your procedure.
    """
    for i in range(1, up_to_number + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizzBuzz(15)
