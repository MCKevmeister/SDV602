import tempfile

def work_with_temporary_file():
	with tempfile.TemporaryFile('w+') as tf:
		tf.write('Order Id 93827, Account Id 286438273')
		tf.seek(0)
		print(tf.read())
		print(tempfile.gettempdir())

if __name__ == "__main__":
	work_with_temporary_file()