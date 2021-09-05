import zipfile
import shutil

def create_zip(files):
	with zipfile.ZipFile('archive.zip', 'w') as archive:
		for file in files:
			archive.write(file)

def append_zip(files):
	with zipfile.ZipFile('archive.zip', 'a') as archive:
		for file in files:
			archive.write(file)

def create_zip_nested_dir(directory_path):
	shutil.make_archive('directory_archive', 'zip', directory_path)

if __name__ == "__main__":
	#files = ["png/monster01.png", "png/monster02.png", "png/monster03.png"]
	#create_zip(files)
	create_zip_nested_dir("svg")