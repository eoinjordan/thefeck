import pytest
from thefeck.rules.python_execute import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('python bar', ''),
    Command('python bar', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('python bar', ''), 'python bar.py'),
    (Command('python bar', ''), 'python bar.py')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
