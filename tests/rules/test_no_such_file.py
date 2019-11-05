import pytest
from thefeck.rules.no_such_file import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('mv bar bar/bar', "mv: cannot move 'bar' to 'bar/bar': No such file or directory"),
    Command('mv bar bar/', "mv: cannot move 'bar' to 'bar/': No such file or directory"),
])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('mv bar bar/', ""),
    Command('mv bar bar/bar', "mv: permission denied"),
])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('mv bar bar/bar', "mv: cannot move 'bar' to 'bar/bar': No such file or directory"), 'mkdir -p bar && mv bar bar/bar'),
    (Command('mv bar bar/', "mv: cannot move 'bar' to 'bar/': No such file or directory"), 'mkdir -p bar && mv bar bar/'),
])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
