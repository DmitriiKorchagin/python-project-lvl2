from gendiff.engine import generate_diff


result_plain = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_gendiff_flat():
    assert result_plain == generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
