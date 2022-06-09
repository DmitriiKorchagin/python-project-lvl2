#!/usr/bin/env python3
""" the Diff Script """
import gendiff.parser
from gendiff.engine import generate_diff


def main():
    diff_result = generate_diff(gendiff.parser.first_file,
                                gendiff.parser.second_file)
    print(diff_result)


if __name__ == '__main__':
    main()
