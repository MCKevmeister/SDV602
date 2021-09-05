import os
from pathlib import Path
import shutil

def rename_os():
	os.rename('images/monster01.png', 'images/monster_01.png')

def rename_pathlib():
	file = Path('images/monster02.png')
	file.rename('images/monster_02.png')

def move_files():
	shutil.move('images/', 'png/')

def move_file():
	os.mkdir('svg')
	shutil.move('png/monster03.svg', 'svg/')

if __name__ == "__main__":
	# rename_os()
	# rename_pathlib()
	move_files()
	move_file()