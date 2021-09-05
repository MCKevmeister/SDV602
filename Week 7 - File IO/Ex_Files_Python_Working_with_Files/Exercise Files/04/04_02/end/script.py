import zipfile

def read_zip():
	with zipfile.ZipFile('archive.zip', 'r') as archive:
		print(archive.namelist())

def retrieve_file_info_zip():
	with zipfile.ZipFile('archive.zip', 'r') as archive:
		file_info = archive.getinfo('description01.txt')
		print(file_info)

def read_file_in_zip():
	with zipfile.ZipFile('archive.zip', 'r') as archive:
		with archive.open('description01.txt') as file:
			print(file.read())

def extract_file(archive, file_to_extract):
	with zipfile.ZipFile(archive, 'r') as my_archive:
		my_archive.extract(file_to_extract)

def extract_all():
	with zipfile.ZipFile('archive.zip', 'r') as archive:
		archive.extractall("extracted_files")

if __name__ == "__main__":
	#read_zip()
	#retrieve_file_info_zip()
	#read_file_in_zip()
	#extract_file('archive.zip', 'description01.txt')
	extract_all()




