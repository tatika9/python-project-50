import itertools
from gendiff.diff_tree import get_status, get_name
from gendiff.diff_tree import get_value, get_children
from gendiff.formatters.value_to_str import value_to_str


def get_stylish(diff, replacer=' ', indent=4):
    FILLER = {
        'added': '+ ',
        'deleted': '- ',
        'unchanged': '  ',
        'nested': '  ',
    }

    def format_value(diff, level):
        if isinstance(diff, dict):
            lines = []
            current_indent = (level * indent - len(FILLER["nested"])) * replacer

            for key, val in diff.items():
                prefix = current_indent + FILLER["nested"]
                value = format_value(val, level + 1)
                lines.append(f'{prefix}{key}: {value}')

            current_indent = (level - 1) * indent * replacer
            result = itertools.chain('{', lines, [current_indent + '}'])
            return '\n'.join(result)
        return value_to_str(diff)

    def inner(diff, level):
        lines = []
        current_indent = (level * indent - len(FILLER["nested"])) * replacer

        for child in get_children(diff):
            status = get_status(child)
            name = get_name(child)

            if status == 'nested':
                prefix = current_indent + FILLER[status]
                value = inner(child, level + 1)
                lines.append(f'{prefix}{name}: {value}')
            elif status == 'changed':
                prefix = current_indent + FILLER["deleted"]
                value = format_value(get_value(child)["old"], level+1)
                lines.append(f'{prefix}{name}: {value}')

                prefix = current_indent + FILLER["added"]
                value = format_value(get_value(child)["new"], level+1)
                lines.append(f'{prefix}{name}: {value}')
            else:
                prefix = current_indent + FILLER[status]
                value = format_value(get_value(child), level+1)
                lines.append(f'{prefix}{name}: {value}')

        current_indent = (level - 1) * indent * replacer
        result = itertools.chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return inner(diff, 1)
