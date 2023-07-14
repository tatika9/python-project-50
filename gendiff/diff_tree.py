def mk_nested(name, children=[]):
    return {
        'name': name,
        'type': 'nested',
        'children': children,
    }


def mk_plain(name, action, value={'old': None, 'new': None}):
    return {
        'name': name,
        'type': 'plain',
        'action': action,
        'value': value,
    }


def is_plain(node):
    return node['type'] == 'plain'


def is_nested(node):
    return node['type'] == 'nested'


def get_name(node):
    return node['name']


def get_value(node):
    return node['value']


def get_action(node):
    return node['action']


def get_children(node):
    return node.get('children', [])
