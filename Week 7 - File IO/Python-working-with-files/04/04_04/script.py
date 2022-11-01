import tarfile


def create_tar_archive():
    files = ['monsters.csv', 'Monster_contact_sheet.pdf']
    with tarfile.open('archive.tar', 'w') as tar:
        for file in files:
            tar.add(file)


def add_to_tar_archive():
    with tarfile.open('archive.tar', 'a') as tar:
        tar.add('monsters_card03.png')


def extract_tar():
    with tarfile.open('archive.tar') as tar:
        tar.extract('monsters_card03.png')


def extract_all():
    with tarfile.open('archive.tar') as tar:
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(tar, "extracted_monster_files")


if __name__ == "__main__":
    # create_tar_archive()
    # add_to_tar_archive()
    # extract_tar()
    extract_all()
