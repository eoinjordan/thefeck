"""Fixes common java command mistake

Example:
> java bar.java
Error: Could not find or load main class bar.java

"""
from thefeck.utils import for_app


@for_app('java')
def match(command):
    return command.script.endswith('.java')


def get_new_command(command):
    return command.script[:-5]
