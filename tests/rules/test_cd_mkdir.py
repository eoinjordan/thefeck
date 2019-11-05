import pytest
from thefeck.rules.cd_mkdir import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('cd bar', 'cd: bar: No such file or directory'),
    Command('cd bar/bar/baz',
            'cd: bar: No such file or directory'),
    Command('cd bar/bar/baz', 'cd: can\'t cd to bar/bar/baz'),
    Command('cd /bar/bar/', 'cd: The directory "/bar/bar/" does not exist')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('cd bar', ''), Command('', '')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('cd bar', ''), 'mkdir -p bar && cd bar'),
    (Command('cd bar/bar/baz', ''), 'mkdir -p bar/bar/baz && cd bar/bar/baz')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
