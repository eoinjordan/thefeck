import pytest
from thefeck.rules.mkdir_p import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('mkdir bar/bar/baz', 'mkdir: bar/bar: No such file or directory'),
    Command('./bin/hdfs dfs -mkdir bar/bar/baz', 'mkdir: `bar/bar/baz\': No such file or directory'),
    Command('hdfs dfs -mkdir bar/bar/baz', 'mkdir: `bar/bar/baz\': No such file or directory')
])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('mkdir bar/bar/baz', ''),
    Command('mkdir bar/bar/baz', 'bar bar baz'),
    Command('hdfs dfs -mkdir bar/bar/baz', ''),
    Command('./bin/hdfs dfs -mkdir bar/bar/baz', ''),
    Command('', ''),
])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('mkdir bar/bar/baz', ''), 'mkdir -p bar/bar/baz'),
    (Command('hdfs dfs -mkdir bar/bar/baz', ''), 'hdfs dfs -mkdir -p bar/bar/baz'),
    (Command('./bin/hdfs dfs -mkdir bar/bar/baz', ''), './bin/hdfs dfs -mkdir -p bar/bar/baz'),
])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
