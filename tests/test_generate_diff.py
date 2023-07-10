from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    with open('tests/fixtures/result_json.txt', 'r') as expected:
        expected = expected.read()
    
    assert generate_diff(file1, file2) == expected
