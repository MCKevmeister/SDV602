def fizzBuzz(up_to_number):

    listoftuples = []
    for i in range(1, up_to_number + 1):
        if i % 3 == 0 and i % 5 == 0:
            listoftuples.append(tuple((i, "FizzBuzz")))
        elif i % 3 == 0:
            listoftuples.append(tuple((i, "Fizz")))
        elif i % 5 == 0:
            listoftuples.append(tuple((i, "Buzz")))
        else:
            listoftuples.append(tuple((i, str(i))))
    return listoftuples


print(fizzBuzz(15))
