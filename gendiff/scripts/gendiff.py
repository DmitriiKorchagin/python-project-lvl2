#!/usr/bin/env python3
""" the Diff Script """
import argparse
import os
from gendiff.engine import generate_diff


parser = argparse.ArgumentParser(description='Compares two configuration\
                                 files and shows a difference.')
parser.add_argument("first_file")
parser.add_argument("second_file")
parser.add_argument("-f", "--format", help="set format of output")
args = parser.parse_args()

first_file = os.path.abspath(args.first_file)
second_file = os.path.abspath(args.second_file)

diff = generate_diff(first_file, second_file)
print(diff)


def main():
    pass


if __name__ == '__main__':
    main()
