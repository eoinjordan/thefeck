import pytest
from thefeck.rules.pip_unknown_command import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def pip_unknown_cmd():
    return '''ERROR: unknown command "instatl" - maybe you meant "install"'''


@pytest.fixture
def pip_unknown_cmd_without_recommend():
    return '''ERROR: unknown command "i"'''


def test_match(pip_unknown_cmd, pip_unknown_cmd_without_recommend):
    assert match(Command('pip instatl', pip_unknown_cmd))
    assert not match(Command('pip i',
                             pip_unknown_cmd_without_recommend))


def test_get_new_command(pip_unknown_cmd):
    assert get_new_command(Command('pip instatl',
                                   pip_unknown_cmd)) == 'pip install'
