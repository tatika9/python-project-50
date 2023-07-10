from gendiff.generate_diff import generate_diff


def test_generate_diff_json():
    file1_json = 'tests/fixtures/file1.json'
    file2_json = 'tests/fixtures/file2.json'
    file1_yaml = 'tests/fixtures/file1.yaml'
    file2_yaml = 'tests/fixtures/file2.yaml'
    with open('tests/fixtures/result.txt', 'r') as expected:
        expected = expected.read()
    
    assert generate_diff(file1_json, file2_json) == expected
    assert generate_diff(file1_yaml, file2_yaml) == expected
