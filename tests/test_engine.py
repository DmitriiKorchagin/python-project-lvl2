from gendiff.engine import generate_diff


result_plain = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_gendiff_flat_json():
    assert result_plain == generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')

def test_gendiff_flat_yaml():
    assert result_plain == generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yaml')

def test_gendiff_flat_yaml_json():
    assert result_plain == generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.yaml')
