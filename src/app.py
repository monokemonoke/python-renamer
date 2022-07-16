from ast import arg
from glob import glob
from os import rename
from tqdm import tqdm
from sys import argv

def input_with_dialogue():
    print('Input file pattern: ', end='')
    file_pattern = input()

    print('Input before str: ', end='')
    replace_from = input()

    print('Input after str: ', end='')
    replace_to = input()

    files = glob(file_pattern)
    for before_name in tqdm(files):
        after_name = before_name.replace(replace_from, replace_to)
        rename(before_name, after_name)

def input_with_args():
    file_pattern = argv[1]
    replace_from = argv[2]
    replace_to = argv[3]

    files = glob(file_pattern)
    for before_name in files:
        after_name = before_name.replace(replace_from, replace_to)
        rename(before_name, after_name)

def main():
    if len(argv) == 1:
        input_with_dialogue()
    elif len(argv) == 4:
        input_with_args()
    else:
        print('Usage:')
        print('\t$ renamer : Dialogue mode')
        print('\t$ renamer <file pattern> <replace text before> <replace text after>')

if __name__ == '__main__':
    main()
