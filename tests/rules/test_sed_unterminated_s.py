import pytest
from thefeck.rules.sed_unterminated_s import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def sed_unterminated_s():
    return "sed: -e expression #1, char 9: unterminated `s' command"


def test_match(sed_unterminated_s):
    assert match(Command('sed -e s/bar/bar', sed_unterminated_s))
    assert match(Command('sed -es/bar/bar', sed_unterminated_s))
    assert match(Command('sed -e s/bar/bar -e s/baz/quz', sed_unterminated_s))
    assert not match(Command('sed -e s/bar/bar', ''))
    assert not match(Command('sed -es/bar/bar', ''))
    assert not match(Command('sed -e s/bar/bar -e s/baz/quz', ''))


def test_get_new_command(sed_unterminated_s):
    assert (get_new_command(Command('sed -e s/bar/bar', sed_unterminated_s))
            == 'sed -e s/bar/bar/')
    assert (get_new_command(Command('sed -es/bar/bar', sed_unterminated_s))
            == 'sed -es/bar/bar/')
    assert (get_new_command(Command(r"sed -e 's/\/bar/bar'", sed_unterminated_s))
            == r"sed -e 's/\/bar/bar/'")
    assert (get_new_command(Command(r"sed -e s/bar/bar -es/baz/quz", sed_unterminated_s))
            == r"sed -e s/bar/bar/ -es/baz/quz/")
