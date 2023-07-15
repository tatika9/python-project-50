import itertools
from gendiff.diff_tree import get_status, get_name
from gendiff.diff_tree import get_value, get_children
from gendiff.formatters.value_to_str import value_to_str


def stylish(diff, replacer=' ', indent=4):
    STATUS = {
        'added': '+ ',
        'deleted': '- ',
        'unchanged': '  ',
        'nested': '  ',
    }

    def format_unchange(diff, level):
        if isinstance(diff, dict):
            lines = []
            current_indent = (level * indent - len(STATUS["nested"])) * replacer
            for key, val in diff.items():
                lines.append(f'{current_indent}{STATUS["nested"]}{key}: '
                             f'{format_unchange(val, level + 1)}')
            current_indent = (level - 1) * indent * replacer
            result = itertools.chain('{', lines, [current_indent + '}'])
            return '\n'.join(result)
        return value_to_str(diff)

    def inner(diff, level):
        children = get_children(diff)
        lines = []
        current_indent = (level * indent - len(STATUS["nested"])) * replacer

        for child in children:
            status = get_status(child)
            if status == 'nested':
                lines.append(
                    f'{current_indent}{STATUS[status]}'
                    f'{get_name(child)}: {inner(child, level + 1)}'
                )
            elif get_status(child) == 'changed':
                lines.append(
                    f'{current_indent}{STATUS["deleted"]}{get_name(child)}: '
                    f'{format_unchange(get_value(child)["old"], level+1)}'
                )
                lines.append(
                    f'{current_indent}{STATUS["added"]}{get_name(child)}: '
                    f'{format_unchange(get_value(child)["new"], level+1)}'
                )
            else:
                lines.append(
                    f'{current_indent}{STATUS[status]}{get_name(child)}: '
                    f'{format_unchange(get_value(child), level+1)}'
                )
        current_indent = (level - 1) * indent * replacer
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return inner(diff, 1)
