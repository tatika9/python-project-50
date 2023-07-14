from gendiff.diff_tree import mk_plain, mk_nested


def get_diff(dict1, dict2):
    def iter(name, node1, node2):
        children = []
        keys = sorted(node1.keys() | node2.keys())
        for key in keys:
            if key not in node1:
                children.append(mk_plain(
                    key, 'added', {'old': None, 'new': node2[key]}
                ))
            elif key not in node2:
                children.append(mk_plain(
                    key, 'deleted', {'old': node1[key], 'new': None}
                ))
            elif isinstance(node1[key], dict) and isinstance(node2[key], dict):
                children.append(iter(key, node1[key], node2[key]))
            elif node1[key] == node2[key]:
                children.append(mk_plain(
                    key, 'unchanged', {'old': node1[key], 'new': node2[key]}
                ))
            else:
                children.append(mk_plain(
                    key, 'changed', {'old': node1[key], 'new': node2[key]}
                ))
        return mk_nested(name, children)
    return iter(None, dict1, dict2)
