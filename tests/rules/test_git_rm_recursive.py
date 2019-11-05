import pytest
from thefeck.rules.git_rm_recursive import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def output(target):
    return "fatal: not removing '{}' recursively without -r".format(target)


@pytest.mark.parametrize('script, target', [
    ('git rm bar', 'bar'),
    ('git rm bar bar', 'bar bar')])
def test_match(output, script, target):
    assert match(Command(script, output))


@pytest.mark.parametrize('script', ['git rm bar', 'git rm bar bar'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, target, new_command', [
    ('git rm bar', 'bar', 'git rm -r bar'),
    ('git rm bar bar', 'bar bar', 'git rm -r bar bar')])
def test_get_new_command(output, script, target, new_command):
    assert get_new_command(Command(script, output)) == new_command
