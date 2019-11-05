import pytest
from thefeck.rules.git_diff_no_index import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('git diff bar bar', '')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('git diff --no-index bar bar', ''),
    Command('git diff bar', ''),
    Command('git diff bar bar baz', '')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('git diff bar bar', ''), 'git diff --no-index bar bar')])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
