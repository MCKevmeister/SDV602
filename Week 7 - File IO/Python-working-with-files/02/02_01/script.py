def print_content():
    with open('descriptions/description-01.txt', 'r') as f:
        contents = f.read()
        print(contents)


def write_new_content():
    with open('descriptions/description-01.txt', 'w') as f:
        f.write("lorum ipusm")


if __name__ == "__main__":
    print_content()
    write_new_content()
