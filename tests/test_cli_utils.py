import pytest
from argparse import ArgumentParser
from unittest.mock import Mock
from httpie.cli.utils import LazyChoices


def test_lazy_choices():
    mock = Mock()
    getter = mock.getter
    getter.return_value = ['a', 'b', 'c']

    parser = ArgumentParser()
    parser.register('action', 'lazy_choices', LazyChoices)
    parser.add_argument(
        '--option',
        help="the regular option",
        default='a',
        metavar='SYMBOL',
        choices=['a', 'b'],
    )
    parser.add_argument(
        '--lazy-option',
        help="the lazy option",
        default='a',
        metavar='SYMBOL',
        action='lazy_choices',
        getter=getter,
        cache=False  # for test purposes
    )

    # Parser initialization doesn't call it.
    getter.assert_not_called()

    # If we don't use --lazy-option, we don't retrieve it.
    parser.parse_args([])
    getter.assert_not_called()

    parser.parse_args(['--option', 'b'])
    getter.assert_not_called()

    # If we pass a value, it will retrieve to verify.
    parser.parse_args(['--lazy-option', 'c'])
    getter.assert_called()
    getter.reset_mock()

    with pytest.raises(SystemExit):
        parser.parse_args(['--lazy-option', 'z'])
    getter.assert_called()
    getter.reset_mock()


def test_lazy_choices_help():
    mock = Mock()
    getter = mock.getter
    getter.return_value = ['a', 'b', 'c']

    help_formatter = mock.help_formatter
    help_formatter.return_value = '<my help>'

    parser = ArgumentParser()
    parser.register('action', 'lazy_choices', LazyChoices)
    parser.add_argument(
        '--lazy-option',
        default='a',
        metavar='SYMBOL',
        action='lazy_choices',
        getter=getter,
        help_formatter=help_formatter,
        cache=False  # for test purposes
    )

    # Parser initialization doesn't call it.
    getter.assert_not_called()

    # If we don't use `--help`, we don't use it.
    parser.parse_args([])
    getter.assert_not_called()
    help_formatter.assert_not_called()

    parser.parse_args(['--lazy-option', 'b'])
    help_formatter.assert_not_called()

    # If we use --help, then we call it with styles
    with pytest.raises(SystemExit):
        parser.parse_args(['--help'])
    help_formatter.assert_called_once_with(['a', 'b', 'c'], isolation_mode=False)


def test_lazy_choices_default_validation_does_not_load_choices():
    mock = Mock()
    getter = mock.getter
    getter.return_value = ['a', 'b', 'c']

    parser = ArgumentParser()
    parser.register('action', 'lazy_choices', LazyChoices)
    parser.add_argument(
        '--lazy-option',
        default='a',
        metavar='SYMBOL',
        action='lazy_choices',
        getter=getter,
        cache=False,  # for test purposes
    )

    action = next(
        action for action in parser._actions
        if action.dest == 'lazy_option'
    )

    # Simulate default validation (as in Python 3.14 parser setup)
    # and ensure it does not trigger eager loading.
    parser._check_value(action, 'a')
    getter.assert_not_called()

    parser._check_value(action, 'b')
    getter.assert_called_once()
