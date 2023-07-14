import itertools
from gendiff.diff_tree import is_nested, get_action, get_name
from gendiff.diff_tree import get_value, get_children


def get_format(diff, format):
    if format == 'stylish':
        return stylish(diff)
    if format == 'plain':
        return plain(diff)


def bool_to_str(text):
    if type(text) == bool:
        return ' ' + str(text).lower()
    if text is None:
        return ' null'
    if text == '':
        return text
    return ' ' + str(text)


def format_plain(value):
    if isinstance(value, (dict, list, tuple, set)):
        return ' [complex value]'
    if isinstance(value, str):
        value = f"'{value}'"
    return bool_to_str(value)


def stylish(diff):
    indent = 4
    prefix_unchange = '  '
    prefix_added = '+ '
    prefix_deleted = '- '

    def format_unchange(diff, level):
        if isinstance(diff, dict):
            lines = []
            current_indent = (level * indent - len(prefix_unchange)) * ' '
            for key, val in diff.items():
                lines.append(f'{current_indent}{prefix_unchange}{key}:'
                             f'{format_unchange(val, level + 1)}')
            current_indent = (level - 1) * indent * ' '
            result = itertools.chain([' {'], lines, [current_indent + '}'])
            return '\n'.join(result)
        return bool_to_str(diff)

    def inner(diff, level):
        children = get_children(diff)
        lines = []
        current_indent = (level * indent - len(prefix_unchange)) * ' '

        for child in children:
            if is_nested(child):
                lines.append(
                    f'{current_indent}{prefix_unchange}'
                    f'{get_name(child)}: {inner(child, level + 1)}'
                )
            elif get_action(child) == 'deleted':
                lines.append(
                    f'{current_indent}{prefix_deleted}{get_name(child)}:'
                    f'{format_unchange(get_value(child)["old"], level+1)}'
                )
            elif get_action(child) == 'added':
                lines.append(
                    f'{current_indent}{prefix_added}{get_name(child)}:'
                    f'{format_unchange(get_value(child)["new"], level+1)}'
                )
            elif get_action(child) == 'changed':
                lines.append(
                    f'{current_indent}{prefix_deleted}{get_name(child)}:'
                    f'{format_unchange(get_value(child)["old"], level+1)}'
                )
                lines.append(
                    f'{current_indent}{prefix_added}{get_name(child)}:'
                    f'{format_unchange(get_value(child)["new"], level+1)}'
                )
            elif get_action(child) == 'unchanged':
                lines.append(
                    f'{current_indent}{prefix_unchange}{get_name(child)}:'
                    f'{format_unchange(get_value(child)["old"], level+1)}'
                )
        current_indent = (level - 1) * indent * ' '
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return inner(diff, 1)


def plain(diff):
    def inner(diff, acc):
        children = get_children(diff)
        lines = []
        for child in children:
            if is_nested(child):
                lines.append(inner(child, acc + get_name(child) + '.'))
            elif get_action(child) == 'deleted':
                lines.append(f'Property \'{acc + get_name(child)}\' was removed')
            elif get_action(child) == 'added':
                lines.append(
                    f'Property \'{acc + get_name(child)}\''
                    f' was added with value:'
                    f'{format_plain(get_value(child)["new"])}'
                )
            elif get_action(child) == 'changed':
                lines.append(
                    f'Property \'{acc + get_name(child)}\' was updated.'
                    f' From{format_plain(get_value(child)["old"])}'
                    f' to{format_plain(get_value(child)["new"])}'
                )
            elif get_action(child) == 'unchanged':
                continue
        return '\n'.join(lines)
    return inner(diff, '')
