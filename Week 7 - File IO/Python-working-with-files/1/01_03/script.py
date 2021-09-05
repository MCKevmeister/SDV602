from datetime import datetime
import os


def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formatted_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formatted_date


def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("Name: ", entry.name)
            info = entry.stat()
            # Unix: print("Creation Time:", info.st_birthtime)
            print("Creation Time: ", format_datetime(info.st_ctime))  # windows
            print("Last Access Time: ", format_datetime(info.st_atime))
            print("Size: ", info.st_size)


def display_direcotries(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory Name: ", entry.name)


def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("Directory Name: ", entry.name)


if __name__ == "__main__":
    display_entries_in_directory("artwork/")
    display_direcotries("artwork/")
    display_files("artwork/")