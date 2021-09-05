import shutil

def copy_file():
	shutil.copy('monster01.png', 'images/png')

def copy_file_with_metadata():
	shutil.copy2('monster02.png', 'images/png')

def copy_directory():
	shutil.copytree('images/', 'back-up-images/')

if __name__ == "__main__":
	# copy_file()
	# copy_file_with_metadata()
	copy_directory()