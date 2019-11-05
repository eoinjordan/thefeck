import pytest
from thefeck.argument_parser import Parser
from thefeck.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['thefeck'], _args()),
    (['thefeck', '-a'], _args(alias='feck')),
    (['thefeck', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='feck', enable_experimental_instant_mode=True)),
    (['thefeck', '-a', 'fix'], _args(alias='fix')),
    (['thefeck', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['thefeck', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['thefeck', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['thefeck', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['thefeck', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['thefeck', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['thefeck', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['thefeck', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
