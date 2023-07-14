def value_to_str(text):
    if type(text) == bool:
        return ' ' + str(text).lower()
    if text is None:
        return ' null'
    if text == '':
        return text
    return ' ' + str(text)
