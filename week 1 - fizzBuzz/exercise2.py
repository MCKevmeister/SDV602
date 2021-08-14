def fizzBuzzExercise2(up_to_number):
    """
    Exercise 2
    2. Rewrite the procedure you produced for exercise 1, without using “for
    i in range( up_to_number )”, use while instead
    """
    result = []
    i: int = 1
    while i < up_to_number + 1:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(int(i))
        i += 1
    return result


fizzBuzzExercise2(15)
