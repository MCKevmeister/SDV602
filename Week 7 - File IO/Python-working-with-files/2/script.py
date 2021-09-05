from datetime import datetime
import os


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date


def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
