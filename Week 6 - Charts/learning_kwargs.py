def someFunction(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(kwargs))


if __name__ == "__main__":
    someFunction("hello", "world", first_arg="first", second_arg="second")
    # ('hello', 'world')
    # {'first_arg': 'first', 'second_arg' = 'second'}
    # <class 'dict'>
