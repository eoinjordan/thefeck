import pytest
from thefeck.rules.dry import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('cd cd bar', ''),
    Command('git git push origin/master', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('cd cd bar', ''), 'cd bar'),
    (Command('git git push origin/master', ''), 'git push origin/master')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
