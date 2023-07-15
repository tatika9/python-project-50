def mk_nested(name, children=[]):
    return {
        'name': name,
        'status': 'nested',
        'children': children,
    }


def mk_plain(name, status, value):
    return {
        'name': name,
        'status': status,
        'value': value,
    }


def is_nested(node):
    return node['status'] == 'nested'


def get_name(node):
    return node['name']


def get_value(node):
    return node['value']


def get_status(node):
    return node['status']


def get_children(node):
    return node.get('children', [])
