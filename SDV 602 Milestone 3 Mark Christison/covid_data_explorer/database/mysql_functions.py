# import mysql.connector
#
#
# def call_mysql_stored_procedure(procedure_name, args):
#     connection = mysql.connector.connect(user='root',
#                                          password='yDEmL9qgmd1H96Or',
#                                          host='sdv602.cbhkwot5prff.ap-southeast-2.rds.amazonaws.com',
#                                          database='sdv602')
#     if connection.is_connected():
#         cursor = connection.cursor()
#         db_message = cursor.callproc(procedure_name, args)
#     connection.close()
#     return db_message
