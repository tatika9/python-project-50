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


def read(file):
    with open(file, 'r') as f:
        return f.read()


def test_generate_diff_plane():
    file1_json = 'tests/fixtures/file1_plane.json'
    file2_json = 'tests/fixtures/file2_plane.json'
    file1_yaml = 'tests/fixtures/file1_plane.yaml'
    file2_yaml = 'tests/fixtures/file2_plane.yaml'

    expected_stylish = read('tests/fixtures/result_plane_stylish.txt')
    expected_plain = read('tests/fixtures/result_plane_plain.txt')

    assert generate_diff(file1_json, file2_json) == expected_stylish
    assert generate_diff(file1_yaml, file2_yaml) == expected_stylish
    assert generate_diff(file1_yaml, file2_yaml, 'stylish') == expected_stylish
    assert generate_diff(file1_json, file2_json, 'plain') == expected_plain
    assert generate_diff(file1_yaml, file2_yaml, 'plain') == expected_plain


def test_generate_diff():
    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    file1_yaml = 'tests/fixtures/file1.yaml'
    file2_yaml = 'tests/fixtures/file2.yaml'

    expected_stylish = read('tests/fixtures/result_stylish.txt')
    expected_plain = read('tests/fixtures/result_plain.txt')

    assert generate_diff(file1_json, file2_json) == expected_stylish
    assert generate_diff(file1_yaml, file2_yaml) == expected_stylish
    assert generate_diff(file1_yaml, file2_yaml, 'stylish') == expected_stylish
    assert generate_diff(file1_json, file2_json, 'plain') == expected_plain
    assert generate_diff(file1_yaml, file2_yaml, 'plain') == expected_plain
