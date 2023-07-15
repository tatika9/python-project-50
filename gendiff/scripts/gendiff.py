#!/usr/bin/env python3

from gendiff.args_parser import parse_arguments
from gendiff.generate_diff import generate_diff


def main():
    file_path1, file_path2, format = parse_arguments()
    print(generate_diff(file_path1, file_path2, format))


if __name__ == '__main__':
    main()
