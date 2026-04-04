import argparse
import io
import sys

import pytest
import shutil
import os
from tests.utils import http


# Detect whether argparse quotes choices in error messages.
# Python 3.12.4+ (and 3.13+) removed the quotes.
def _argparse_quotes_choices():
    p = argparse.ArgumentParser(prog='_probe')
    p.add_argument('--c', choices=['x'])
    buf = io.StringIO()
    saved = sys.stderr
    sys.stderr = buf
    try:
        p.parse_args(['--c', 'z'])
    except SystemExit:
        pass
    finally:
        sys.stderr = saved
    return "'x'" in buf.getvalue()


def _fmt_argparse_choice(choice):
    return f"'{choice}'" if _ARGPARSE_QUOTES else choice


_ARGPARSE_QUOTES = _argparse_quotes_choices()

NAKED_BASE_TEMPLATE = """\
usage:
    http {extra_args}[METHOD] URL [REQUEST_ITEM ...]

error:
    {error_msg}

for more information:
    run 'http --help' or visit https://httpie.io/docs/cli

"""

NAKED_HELP_MESSAGE = NAKED_BASE_TEMPLATE.format(
    extra_args="",
    error_msg="the following arguments are required: URL"
)

NAKED_HELP_MESSAGE_PRETTY_WITH_NO_ARG = NAKED_BASE_TEMPLATE.format(
    extra_args="--pretty {all, colors, format, none} ",
    error_msg="argument --pretty: expected one argument"
)

NAKED_HELP_MESSAGE_PRETTY_WITH_INVALID_ARG = NAKED_BASE_TEMPLATE.format(
    extra_args="--pretty {all, colors, format, none} ",
    error_msg=(
        f"argument --pretty: invalid choice: '$invalid' "
        f"(choose from {_fmt_argparse_choice('all')}, {_fmt_argparse_choice('colors')}, "
        f"{_fmt_argparse_choice('format')}, {_fmt_argparse_choice('none')})"
    )
)


PREDEFINED_TERMINAL_SIZE = (200, 100)


@pytest.fixture(scope="function")
def ignore_terminal_size(monkeypatch):
    """Some tests wrap/crop the output depending on the
    size of the executed terminal, which might not be consistent
    through all runs.

    This fixture ensures every run uses the same exact configuration.
    """

    def fake_terminal_size(*args, **kwargs):
        return os.terminal_size(PREDEFINED_TERMINAL_SIZE)

    # Setting COLUMNS as an env var is required for 3.8<
    monkeypatch.setitem(os.environ, 'COLUMNS', str(PREDEFINED_TERMINAL_SIZE[0]))
    monkeypatch.setattr(shutil, 'get_terminal_size', fake_terminal_size)
    monkeypatch.setattr(os, 'get_terminal_size', fake_terminal_size)


@pytest.mark.parametrize(
    'args, expected_msg', [
        ([], NAKED_HELP_MESSAGE),
        (['--pretty'], NAKED_HELP_MESSAGE_PRETTY_WITH_NO_ARG),
        (['pie.dev', '--pretty'], NAKED_HELP_MESSAGE_PRETTY_WITH_NO_ARG),
        (['--pretty', '$invalid'], NAKED_HELP_MESSAGE_PRETTY_WITH_INVALID_ARG),
    ]
)
def test_naked_invocation(ignore_terminal_size, args, expected_msg):
    result = http(*args, tolerate_error_exit_status=True)
    assert result.stderr == expected_msg
