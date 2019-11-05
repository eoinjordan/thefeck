import pytest
from thefeck.rules.git_remote_delete import get_new_command, match
from thefeck.types import Command


def test_match():
    assert match(Command('git remote delete bar', ''))


@pytest.mark.parametrize('command', [
    Command('git remote remove bar', ''),
    Command('git remote add bar', ''),
    Command('git commit', '')
])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('git remote delete bar', ''), 'git remote remove bar'),
    (Command('git remote delete delete', ''), 'git remote remove delete'),
])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
