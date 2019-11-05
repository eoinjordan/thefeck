import pytest
from thefeck.rules.git_rm_local_modifications import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def output(target):
    return ('error: the following file has local modifications:\n    {}\n(use '
            '--cached to keep the file, or -f to force removal)').format(target)


@pytest.mark.parametrize('script, target', [
    ('git rm bar', 'bar'),
    ('git rm bar bar', 'bar')])
def test_match(output, script, target):
    assert match(Command(script, output))


@pytest.mark.parametrize('script', ['git rm bar', 'git rm bar bar', 'git rm'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, target, new_command', [
    ('git rm bar', 'bar', ['git rm --cached bar', 'git rm -f bar']),
    ('git rm bar bar', 'bar', ['git rm --cached bar bar', 'git rm -f bar bar'])])
def test_get_new_command(output, script, target, new_command):
    assert get_new_command(Command(script, output)) == new_command
