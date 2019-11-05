import pytest
from thefeck.rules.rm_dir import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('rm bar', 'rm: bar: is a directory'),
    Command('rm bar', 'rm: bar: Is a directory'),
    Command('hdfs dfs -rm bar', 'rm: `bar`: Is a directory'),
    Command('./bin/hdfs dfs -rm bar', 'rm: `bar`: Is a directory'),
])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('rm bar', ''),
    Command('hdfs dfs -rm bar', ''),
    Command('./bin/hdfs dfs -rm bar', ''),
    Command('', ''),
])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('rm bar', ''), 'rm -rf bar'),
    (Command('hdfs dfs -rm bar', ''), 'hdfs dfs -rm -r bar'),
])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
