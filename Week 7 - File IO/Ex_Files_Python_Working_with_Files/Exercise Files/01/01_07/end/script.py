import os
from pathlib import Path

def make_logs_dir():
	try:
		os.mkdir("logs/")
	except FileExistsError as ex:
		print("Logs directory already exists")

def make_output_dir():
	dir_path = Path("output/")
	dir_path.mkdir(exist_ok=True)

if __name__ == "__main__":
	# make_logs_dir()
	make_output_dir()