
def print_file_content():
	with open('descriptions/description-01.txt', 'r') as f:
		print(f.read(10))

def print_file_content_readlines():
	with open('descriptions/description-01.txt', 'r') as f:
		lines = f.readlines()
		print(lines[1])

def print_file_content_one_line_at_time():
	with open('descriptions/description-01.txt', 'r') as f:
		line = f.readline()
		while line != '':
			print(line, end='')
			line = f.readline()

if __name__ == "__main__":
	print_file_content_one_line_at_time()