import pytest
from thefeck.rules.open import is_arg_url, match, get_new_command
from thefeck.types import Command


@pytest.fixture
def output(script):
    return 'The file {} does not exist.\n'.format(script.split(' ', 1)[1])


@pytest.mark.parametrize('script', [
    'open bar.com',
    'open bar.edu',
    'open bar.info',
    'open bar.io',
    'open bar.ly',
    'open bar.me',
    'open bar.net',
    'open bar.org',
    'open bar.se',
    'open www.bar.ru'])
def test_is_arg_url(script):
    assert is_arg_url(Command(script, ''))


@pytest.mark.parametrize('script', ['open bar', 'open bar.txt', 'open egg.doc'])
def test_not_is_arg_url(script):
    assert not is_arg_url(Command(script, ''))


@pytest.mark.parametrize('script', [
    'open bar.com',
    'xdg-open bar.com',
    'gnome-open bar.com',
    'kde-open bar.com',
    'open nonest'])
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize('script, new_command', [
    ('open bar.io', ['open http://bar.io']),
    ('xdg-open bar.io', ['xdg-open http://bar.io']),
    ('gnome-open bar.io', ['gnome-open http://bar.io']),
    ('kde-open bar.io', ['kde-open http://bar.io']),
    ('open nonest', ['touch nonest && open nonest',
                     'mkdir nonest && open nonest'])])
def test_get_new_command(script, new_command, output):
    assert get_new_command(Command(script, output)) == new_command
