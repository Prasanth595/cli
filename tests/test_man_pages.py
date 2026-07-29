"""Tests for httpie.output.ui.man_pages."""

import sys
from unittest import mock

import pytest

from httpie.output.ui.man_pages import is_available


class TestIsAvailable:
    """Tests for the is_available() function."""

    def test_returns_false_on_windows(self):
        """is_available() should return False on Windows."""
        with mock.patch.object(sys, 'platform', 'win32'):
            assert is_available('http') is False

    def test_returns_false_when_no_man_pages_env_set(self):
        """is_available() should return False when HTTPIE_NO_MAN_PAGES is set."""
        with mock.patch.dict('os.environ', {'HTTPIE_NO_MAN_PAGES': '1'}):
            assert is_available('http') is False

    def test_returns_true_when_man_exists(self):
        """is_available() should return True when man command exists."""
        with mock.patch.object(sys, 'platform', 'linux'):
            with mock.patch('httpie.output.ui.man_pages.subprocess.run') as mock_run:
                mock_run.return_value = mock.Mock(returncode=0)
                assert is_available('http') is True
                mock_run.assert_called_once_with(
                    ['man', '1', 'http'],
                    shell=False,
                    stdout=mock.ANY,
                    stderr=mock.ANY,
                )

    def test_returns_false_when_man_not_found(self):
        """is_available() should return False when man command fails."""
        with mock.patch.object(sys, 'platform', 'linux'):
            with mock.patch('httpie.output.ui.man_pages.subprocess.run') as mock_run:
                mock_run.return_value = mock.Mock(returncode=1)
                assert is_available('http') is False

    def test_returns_false_on_subprocess_exception(self):
        """is_available() should return False when subprocess raises."""
        with mock.patch.object(sys, 'platform', 'linux'):
            with mock.patch('httpie.output.ui.man_pages.subprocess.run') as mock_run:
                mock_run.side_effect = FileNotFoundError()
                assert is_available('http') is False
