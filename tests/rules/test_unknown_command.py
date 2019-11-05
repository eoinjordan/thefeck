import pytest
from thefeck.rules.unknown_command import match, get_new_command
from thefeck.types import Command


@pytest.mark.parametrize('command', [
    Command('./bin/hdfs dfs ls', 'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.'),
    Command('hdfs dfs ls',
            'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.'),
    Command('hdfs dfs ls /bar/bar', 'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command('./bin/hdfs dfs -ls', ''),
    Command('./bin/hdfs dfs -ls /bar/bar', ''),
    Command('hdfs dfs -ls -R /bar/bar', ''),
    Command('', '')])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command, new_command', [
    (Command('hdfs dfs ls',
             'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.'), ['hdfs dfs -ls']),
    (Command('hdfs dfs rm /bar/bar',
             'rm: Unknown command\nDid you mean -rm?  This command begins with a dash.'), ['hdfs dfs -rm /bar/bar']),
    (Command('./bin/hdfs dfs ls -R /bar/bar',
             'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.'), ['./bin/hdfs dfs -ls -R /bar/bar']),
    (Command('./bin/hdfs dfs -Dtest=fred ls -R /bar/bar',
             'ls: Unknown command\nDid you mean -ls?  This command begins with a dash.'), ['./bin/hdfs dfs -Dtest=fred -ls -R /bar/bar'])])
def test_get_new_command(command, new_command):
    assert get_new_command(command) == new_command
