import argparse


def gendiff():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help = 'set format of output')

    return parser.parse_args()
