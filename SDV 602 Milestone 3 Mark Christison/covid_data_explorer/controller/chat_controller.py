# from mysql_functions import *
# import datetime
#
#
# def send_message(message, username):
#     current_time = datetime.datetime.now()
#     args = (username, message, current_time)
#     db_message = call_mysql_stored_procedure('SendMessage', args)
#     return db_message
#
#
# def get_messages():
#     db_message = call_mysql_stored_procedure('GetMessages', ())
#     return db_message
