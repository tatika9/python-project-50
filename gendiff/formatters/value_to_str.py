def value_to_str(text):
    if isinstance(text, bool):
        return str(text).lower()
    if text is None:
        return 'null'
    return str(text)
