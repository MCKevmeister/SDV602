import mysql.connector


def create_account(username, password, email):
    args = (username, password, email)

    connection = mysql.connector.connect(option_files='my.conf')

    if connection.is_connected():
        cursor = connection.cursor()
        return cursor.callproc('RegisterUser', args)
    connection.close()


def login(username, password):
    # TODO
    return 0


def logout():
    # TODO
    return 0
