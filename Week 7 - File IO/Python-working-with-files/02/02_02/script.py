
def print_file_content():
	with open('descriptions/description-01.txt', 'r') as f:
		print(f.read())

if __name__ == "__main__":
	print_file_content()