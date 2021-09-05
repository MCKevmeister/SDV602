
def print_content():
	with open('descriptions/description-01.txt', 'r') as f:
		contents = f.read()
		print(contents)

def write_new_content():
	with open('descriptions/description-01.txt', 'w') as f:
		f.write("Yodel grew up in a family of singers and loud talkers and could never get a word in edgewise")

if __name__ == "__main__":
	write_new_content()
	print_content()