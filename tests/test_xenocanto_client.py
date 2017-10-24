import urllib.parse
from xenocanto_client import core


def test_generate_query_string_prepends_basic_query():
    query_string = core.generate_query_string('blue jay', {'cnt': 'canada', 'q': 'A'})
    assert query_string == urllib.parse.quote('blue jay cnt:canada q:A', safe=':')


def test_generate_query_string_ignores_basic_if_empty():
    query_string = core.generate_query_string('', {'cnt': 'canada', 'q': 'A'})
    assert query_string == urllib.parse.quote('cnt:canada q:A', safe=':')


def test_generate_query_string_ignores_query_if_empty():
    query_string = core.generate_query_string('blue jay', {})
    assert query_string == urllib.parse.quote('blue jay', safe=':')
