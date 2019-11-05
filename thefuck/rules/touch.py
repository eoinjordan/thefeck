import re
from thefeck.shells import shell
from thefeck.utils import for_app


@for_app('touch')
def match(command):
    return 'No such file or directory' in command.output


def get_new_command(command):
    path = path = re.findall(
        r"touch: (?:cannot touch ')?(.+)/.+'?:", command.output)[0]
    return shell.and_(u'mkdir -p {}'.format(path), command.script)
