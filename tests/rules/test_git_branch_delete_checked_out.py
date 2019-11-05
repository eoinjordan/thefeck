import pytest
from thefeck.rules.git_branch_delete_checked_out import match, get_new_command
from thefeck.types import Command


@pytest.fixture
def output():
    return "error: Cannot delete branch 'bar' checked out at '/bar/bar'"


@pytest.mark.parametrize("script", ["git branch -d bar", "git branch -D bar"])
def test_match(script, output):
    assert match(Command(script, output))


@pytest.mark.parametrize("script", ["git branch -d bar", "git branch -D bar"])
def test_not_match(script):
    assert not match(Command(script, "Deleted branch bar (was a1b2c3d)."))


@pytest.mark.parametrize(
    "script, new_command",
    [
        ("git branch -d bar", "git checkout master && git branch -D bar"),
        ("git branch -D bar", "git checkout master && git branch -D bar"),
    ],
)
def test_get_new_command(script, new_command, output):
    assert get_new_command(Command(script, output)) == new_command
