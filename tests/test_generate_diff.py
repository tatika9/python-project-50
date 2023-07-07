from gendiff.generate_diff import generate_diff, lower_bool


def test_lower_bool():
    assert lower_bool(True) == 'true'
