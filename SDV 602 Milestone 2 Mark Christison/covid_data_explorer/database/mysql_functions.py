import mysql.connector


def call_mysql_stored_procedure(procedure_name, args):
    connection = mysql.connector.connect(host='localhost',
                                         database='PythonDataExplorerDB',
                                         user='root',
                                         password='W7oUmiLaiTrznc',
                                         port=3306)
    if connection.is_connected():
        cursor = connection.cursor()
        db_message = cursor.callproc(procedure_name, args)
    connection.close()
    return db_message
