import pytest
from thefeck.types import Command
from thefeck.rules.brew_update_formula import get_new_command, match


output = ("Error: This command updates brew itself, and does not take formula"
          " names.\nUse 'brew upgrade thefeck'.")


def test_match():
    command = Command('brew update thefeck', output)
    assert match(command)


@pytest.mark.parametrize('script', [
    'brew upgrade bar',
    'brew update'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, formula, ', [
    ('brew update bar', 'bar'),
    ('brew update bar zap', 'bar zap')])
def test_get_new_command(script, formula):
    command = Command(script, output)
    new_command = 'brew upgrade {}'.format(formula)
    assert get_new_command(command) == new_command
