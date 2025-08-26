"""Utilities for linters handling."""

import shlex
import subprocess
import sys
from typing import Tuple

from typing_extensions import Literal


def run_linter_and_get_output(
    linter_command: str,
    files: Tuple[str, ...],
    linter_output: Literal['stdout', 'stderr'],
) -> str:
    """Execute linter command against files and return its output."""
    linter_process = subprocess.run(
        [*shlex.split(linter_command), *files],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    
    if linter_process.returncode != 0:
        print(
            'Unexpected linter exit status. Maybe linter internal error?\n'
            f'return code: {linter_process.returncode}\n'
            f'stdout: {linter_process.stdout}\n'
            f'stderr: {linter_process.stderr}\n',
        )
        sys.exit(1)
    
    if linter_output == 'stdout':
        output = linter_process.stdout
    else:
        output = linter_process.stderr
    return output
