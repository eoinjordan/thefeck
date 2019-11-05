import pytest
from thefeck.rules.cd_correction import match
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


# Note that get_new_command uses local filesystem, so not testing it here.
# Instead, see the functional test `functional.test_cd_correction`
