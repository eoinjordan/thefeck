import pytest
from thefeck.rules.javac import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('javac bar', ''),
    Command('javac bar', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('javac bar', ''), 'javac bar.java'),
    (Command('javac bar', ''), 'javac bar.java')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
