import tempfile


def work_with_temp_file():
    with tempfile.TemporaryFile('w+') as tf:
        tf.write('Order 7898797, Account id 944397349743975')
        tf.seek(0)
        print(tf.read())
        print(tempfile.gettempdir())


if __name__ == '__main__':
    work_with_temp_file()