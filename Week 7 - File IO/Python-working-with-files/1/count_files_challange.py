import os


def count_subdirectories():
    count: int = 0
    for files in os.walk(os.getcwd()):
        for _ in files:
            count += 1
    print(count)


if __name__ == '__main__':
    count_subdirectories()
