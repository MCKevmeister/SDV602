import glob

def find_most_common_word():
	txt_files = glob.glob('*.txt')
	tracker = dict()
	print(f"Number of Txt Files: {len(txt_files)}")

	for txt in txt_files:
		with open(txt) as f:
			line = f.readline()
			while line != '':
				words = line.split()
				for word in words:
					word = word.replace(',','').replace('.', '').lower()
					if word not in tracker:
						tracker[word] = 1
					else:
						tracker[word] = tracker[word] + 1
				line = f.readline()

	maxKey = max(tracker, key=tracker.get)
	maxValue = max(tracker.values())

	print(f"Most common word: {maxKey}")
	print(f"How many times: {maxValue}")
	print(f"Dictionary: {tracker}")

if __name__ == "__main__":
	find_most_common_word()






