from gendiff.generate_diff import generate_diff
from gendiff.convert_file_to_python import convert


def test_convert():
    file = 'tests/fixtures/file1.json'
    expected = {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'key': 'value',
                'doge': {
                    'wow': ''
                }
            }
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {
                'key': 'value'
            }
        },
        'group2': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    }

    assert convert(file) == expected


def test_generate_diff_plane():
    file1_json = 'tests/fixtures/file1_plane.json'
    file2_json = 'tests/fixtures/file2_plane.json'
    file1_yaml = 'tests/fixtures/file1_plane.yaml'
    file2_yaml = 'tests/fixtures/file2_plane.yaml'
    with open('tests/fixtures/result_plane.txt', 'r') as expected:
        expected = expected.read()

    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected


def test_generate_diff():
    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    file1_yaml = 'tests/fixtures/file1.yaml'
    file2_yaml = 'tests/fixtures/file2.yaml'
    with open('tests/fixtures/result.txt', 'r') as expected:
        expected = expected.read()

    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected
