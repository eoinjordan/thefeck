import pytest
from thefeck.rules.apt_get_search import get_new_command, match
from thefeck.types import Command


def test_match():
    assert match(Command('apt-get search bar', ''))


@pytest.mark.parametrize('command', [
    Command('apt-cache search bar', ''),
    Command('aptitude search bar', ''),
    Command('apt search bar', ''),
    Command('apt-get install bar', ''),
    Command('apt-get source bar', ''),
    Command('apt-get clean', ''),
    Command('apt-get remove', ''),
    Command('apt-get update', '')
])
def test_not_match(command):
    assert not match(command)


def test_get_new_command():
    new_command = get_new_command(Command('apt-get search bar', ''))
    assert new_command == 'apt-cache search bar'
