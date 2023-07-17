from importlib.metadata import version, metadata
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        help='output format (stylish (default), plain, json)'
    )
    parser.add_argument(
        '-V, --version',
        action='version',
        version=(f'{metadata("hexlet-code")["Name"]} '
                 f'version {version("hexlet-code")}'),
        help='package version'
    )
    args = parser.parse_args()

    return args.first_file, args.second_file, args.format
