"""Fixes error for commands containing the shell prompt symbol '$'.

This usually happens when commands are copied from documentations
including them in their code blocks.

Example:
> $ git clone https://github.com/nvbn/thefeck.git
bash: $: command not found...
"""

import re


def match(command):
    return (
        "$: command not found" in command.output
        and re.search(r"^[\s]*\$ [\S]+", command.script) is not None
    )


def get_new_command(command):
    return command.script.replace("$", "", 1).strip()
