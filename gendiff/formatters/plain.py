from gendiff.diff_tree import is_nested, get_status, get_name
from gendiff.diff_tree import get_value, get_children
from gendiff.formatters.value_to_str import value_to_str


def format_value(value):
    if isinstance(value, (dict, list, tuple, set)):
        return '[complex value]'
    if isinstance(value, str):
        value = f"'{value}'"
    return value_to_str(value)


def get_plain(diff):
    def inner(diff, acc):
        lines = []
        for child in get_children(diff):
            status = get_status(child)
            name = get_name(child)
            if is_nested(child):
                lines.append(inner(child, acc + name + '.'))
            elif status == 'deleted':
                lines.append(f'Property \'{acc + name}\' was removed')
            elif status == 'added':
                lines.append(
                    f'Property \'{acc + name}\''
                    f' was added with value: '
                    f'{format_value(get_value(child))}'
                )
            elif status == 'changed':
                lines.append(
                    f'Property \'{acc + name}\' was updated.'
                    f' From {format_value(get_value(child)["old"])}'
                    f' to {format_value(get_value(child)["new"])}'
                )
            elif status == 'unchanged':
                continue
        return '\n'.join(lines)
    return inner(diff, '')
