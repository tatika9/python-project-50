from gendiff.diff_tree import is_nested, get_action, get_name
from gendiff.diff_tree import get_value, get_children
from gendiff.formatters.value_to_str import value_to_str


def format_value(value):
    if isinstance(value, (dict, list, tuple, set)):
        return ' [complex value]'
    if isinstance(value, str):
        value = f"'{value}'"
    return value_to_str(value)


def plain(diff):
    def inner(diff, acc):
        children = get_children(diff)
        lines = []
        for child in children:
            if is_nested(child):
                lines.append(inner(child, acc + get_name(child) + '.'))
            elif get_action(child) == 'deleted':
                lines.append(
                    f'Property \'{acc + get_name(child)}\' was removed'
                )
            elif get_action(child) == 'added':
                lines.append(
                    f'Property \'{acc + get_name(child)}\''
                    f' was added with value:'
                    f'{format_value(get_value(child)["new"])}'
                )
            elif get_action(child) == 'changed':
                lines.append(
                    f'Property \'{acc + get_name(child)}\' was updated.'
                    f' From{format_value(get_value(child)["old"])}'
                    f' to{format_value(get_value(child)["new"])}'
                )
            elif get_action(child) == 'unchanged':
                continue
        return '\n'.join(lines)
    return inner(diff, '')
