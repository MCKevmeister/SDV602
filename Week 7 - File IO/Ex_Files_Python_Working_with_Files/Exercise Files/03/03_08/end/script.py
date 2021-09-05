from pathlib import Path
from datetime import datetime

def generate_creation_date(path):
	stat_result = path.stat()
	creation_date = stat_result.st_birthtime
	# Windows --> stat_result.st_ctime
	# Other Unix --> stat_result.st_ctime (last modification date)
	# Other Linux --> stat_result.st_mtime (last modification date)
	utc_timestamp = datetime.utcfromtimestamp(creation_date)
	return utc_timestamp.strftime('%Y_%m_%d_')

def organize_images(image_folder):
	file_types = ['.png', '.svg']
	for path in Path(image_folder).iterdir():
		if path.is_file() and path.suffix in file_types:
			print(f"Renaming file {path.stem}")
			date = generate_creation_date(path)
			new_path = Path(image_folder + date + path.stem + path.suffix)
			path.rename(new_path)

if __name__ == "__main__":
	organize_images('./images/')


