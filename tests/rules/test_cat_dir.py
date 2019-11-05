import pytest
from thefeck.rules.cat_dir import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def isdir(mocker):
    return mocker.patch('thefeck.rules.cat_dir'
                        '.os.path.isdir')


@pytest.mark.parametrize('command', [
    Command('cat bar', 'cat: bar: Is a directory\n'),
    Command('cat /bar/bar/', 'cat: /bar/bar/: Is a directory\n'),
    Command('cat cat/', 'cat: cat/: Is a directory\n'),
])
def test_match(command, isdir):
    isdir.return_value = True
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('cat bar', 'bar bar baz'),
    Command('cat bar bar', 'bar bar baz'),
    Command('notcat bar bar', 'some output'),
])
def test_not_match(command, isdir):
    isdir.return_value = False
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('cat bar', 'cat: bar: Is a directory\n'), 'ls bar'),
    (Command('cat /bar/bar/', 'cat: /bar/bar/: Is a directory\n'), 'ls /bar/bar/'),
    (Command('cat cat', 'cat: cat: Is a directory\n'), 'ls cat'),
])
def test_get_new_command(command, new_command):
    isdir.return_value = True
    assert get_new_command(command) == new_command
