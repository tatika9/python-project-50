from gendiff.formatters.stylish import get_stylish
from gendiff.formatters.plain import get_plain
from gendiff.formatters.json import get_json


def get_format(diff, format):
    if format == 'stylish':
        return get_stylish(diff)
    elif format == 'plain':
        return get_plain(diff)
    elif format == 'json':
        return get_json(diff)
    else:
        return (f'{format} is an invalid format. '
                f'Possible options: stylish, plain, json')
