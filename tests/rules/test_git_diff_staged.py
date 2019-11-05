import pytest
from thefeck.rules.git_diff_staged import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('git diff bar', ''),
    Command('git diff', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('git diff --staged', ''),
    Command('git tag', ''),
    Command('git branch', ''),
    Command('git log', '')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('git diff', ''), 'git diff --staged'),
    (Command('git diff bar', ''), 'git diff --staged bar')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
