import re
from thefeck.utils import replace_command
from thefeck.specific.git import git_support


@git_support
def match(command):
    return ('bisect' in command.script_parts and
            'usage: git bisect' in command.output)


@git_support
def get_new_command(command):
    broken = re.findall(r'git bisect ([^ $]*).*', command.script)[0]
    usage = re.findall(r'usage: git bisect \[([^\]]+)\]', command.output)[0]
    return replace_command(command, broken, usage.split('|'))
