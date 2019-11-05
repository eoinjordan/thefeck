import pytest
from thefeck.rules.java import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('java bar.java', ''),
    Command('java bar.java', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('java bar.java', ''), 'java bar'),
    (Command('java bar.java', ''), 'java bar')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
