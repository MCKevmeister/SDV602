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
			info = entry.stat()
			print("Creation Time:", format_datetime(info.st_birthtime))
			# Windows: print("Creation Time: ", info.st_ctime)
			print("Last Access Time:", format_datetime(info.st_atime))
			print("Size:", info.st_size)

def display_directories(directory):
	with os.scandir(directory) as entries:
		for entry in entries:
			if entry.is_dir():
				print("Directory Name:", entry.name)

def display_files(directory):
	with os.scandir(directory) as entries:
		for entry in entries:
			if entry.is_file():
				print("File Name:", entry.name)

if __name__ == "__main__":
	# display_entries_in_directory("artwork/")
	display_directories('artwork/')
	display_files('artwork/')










