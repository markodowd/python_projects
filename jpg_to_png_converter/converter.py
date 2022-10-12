import sys
import os
from PIL import Image


def directory_exists(directory):
    return os.path.exists(directory)


def create_directory(directory):
    if not directory_exists(directory):
        os.makedirs(directory)


def remove_extension_from_filename(filename):
    return os.path.splitext(filename)[0]


def convert_files(path, directory):
    for filename in os.listdir(path):
        clean_name = remove_extension_from_filename(filename)
        img = Image.open(f'{path}/{filename}')
        img.save(f'{directory}/{clean_name}.png', 'png')


def main():
    path = sys.argv[1]
    directory = sys.argv[2]

    create_directory(directory)
    convert_files(path, directory)

    print("finished")


if __name__ == '__main__':
    main()
