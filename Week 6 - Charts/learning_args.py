def add(*args):
    global result
    for number in args:
        result: int = result + number
    return result


def get_type(*args):
    print(type(args))


if __name__ == "__main__":
    total = add(1, 2, 3, 4)
    print(total)  # 10
    get_type("first argument", 1, 7)  # <class 'tuple'>
