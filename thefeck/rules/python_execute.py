# Appends .py when executing python files
#
# Example:
# > python bar
# error: python: can't open file 'bar': [Errno 2] No such file or directory
from thefeck.utils import for_app


@for_app('python')
def match(command):
    return not command.script.endswith('.py')


def get_new_command(command):
    return command.script + '.py'
