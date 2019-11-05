"""Appends .java when compiling java files

Example:
 > javac bar
 error: Class names, 'bar', are only accepted if annotation
 processing is explicitly requested

"""
from thefeck.utils import for_app


@for_app('javac')
def match(command):
    return not command.script.endswith('.java')


def get_new_command(command):
    return command.script + '.java'
