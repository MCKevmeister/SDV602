
def write_content():
	with open('num-series.txt', 'w') as writer:
		for x in range(50):
			content = f'{x}\n'
			writer.write(content)

def append_content():
	with open('num-series.txt', 'a') as writer:
		for x in range(50, 100):
			content = f'{x}\n'
			writer.write(content)

if __name__ == "__main__":
	write_content()
	append_content()