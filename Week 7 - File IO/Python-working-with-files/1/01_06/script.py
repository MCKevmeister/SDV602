# Object oriented interface to the file system
# pathlib operations are as efficient as many os module operations
# more data returned per operation - not just a string

from pathlib import Path


def print_directory_contents():
    entries = Path.cwd()

    # entries = Path('images/')
    # entries = Path.home()

    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent)
        print(entry.parent.parent)
        print(entry.stem)
        print(entry.suffix)
        print(entry.stat())
        print()


if __name__ == "__main__":
    print_directory_contents()
