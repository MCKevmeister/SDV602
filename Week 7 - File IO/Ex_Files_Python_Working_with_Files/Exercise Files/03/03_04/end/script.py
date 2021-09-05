import os
from pathlib import Path
import shutil

def delete_file_os():
	os.remove('screenshots/screenshot1.png')
	# os.unlink('screenshots/screenshot1.png')

def delete_file_pathlib():
	file = Path("screenshots/screenshot2.png")
	file.unlink()

def delete_directory_os():
	os.rmdir("screenshots/")

def delete_directory_pathlib():
	directory = Path("other-screenshots/")
	directory.rmdir()

def delete_directory_including_subdir():
	shutil.rmtree('old-images/')

if __name__ == "__main__":
	# delete_file_os()
	# delete_file_pathlib()
	# delete_directory_os()
	# delete_directory_pathlib()
	delete_directory_including_subdir()









