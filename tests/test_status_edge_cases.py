"""Test edge cases for HTTP status code handling."""
import pytest
from httpie.status import ExitStatus, http_status_to_exit_status


def test_informational_status_codes():
    """Test that 1xx status codes are handled correctly."""
    # 1xx Informational responses should return SUCCESS for 2xx-like behavior
    # or could be considered as SUCCESS since they're not errors
    assert http_status_to_exit_status(100) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(101) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(102) == ExitStatus.SUCCESS


def test_success_status_codes():
    """Test that 2xx status codes return SUCCESS."""
    assert http_status_to_exit_status(200) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(201) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(204) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(299) == ExitStatus.SUCCESS


def test_redirect_status_codes_without_follow():
    """Test that 3xx status codes return ERROR_HTTP_3XX when not following."""
    assert http_status_to_exit_status(300, follow=False) == ExitStatus.ERROR_HTTP_3XX
    assert http_status_to_exit_status(301, follow=False) == ExitStatus.ERROR_HTTP_3XX
    assert http_status_to_exit_status(302, follow=False) == ExitStatus.ERROR_HTTP_3XX
    assert http_status_to_exit_status(399, follow=False) == ExitStatus.ERROR_HTTP_3XX


def test_redirect_status_codes_with_follow():
    """Test that 3xx status codes return SUCCESS when following redirects."""
    assert http_status_to_exit_status(300, follow=True) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(301, follow=True) == ExitStatus.SUCCESS
    assert http_status_to_exit_status(302, follow=True) == ExitStatus.SUCCESS


def test_client_error_status_codes():
    """Test that 4xx status codes return ERROR_HTTP_4XX."""
    assert http_status_to_exit_status(400) == ExitStatus.ERROR_HTTP_4XX
    assert http_status_to_exit_status(404) == ExitStatus.ERROR_HTTP_4XX
    assert http_status_to_exit_status(499) == ExitStatus.ERROR_HTTP_4XX


def test_server_error_status_codes():
    """Test that 5xx status codes return ERROR_HTTP_5XX."""
    assert http_status_to_exit_status(500) == ExitStatus.ERROR_HTTP_5XX
    assert http_status_to_exit_status(503) == ExitStatus.ERROR_HTTP_5XX
    assert http_status_to_exit_status(599) == ExitStatus.ERROR_HTTP_5XX


def test_invalid_status_codes():
    """Test that invalid/unknown status codes are handled.

    Status codes outside the standard ranges (600+, negative, etc.)
    should return an error status rather than SUCCESS.
    """
    # Status codes >= 600 are not defined in HTTP spec
    result = http_status_to_exit_status(600)
    assert result == ExitStatus.ERROR

    result = http_status_to_exit_status(999)
    assert result == ExitStatus.ERROR

    # Negative status codes don't make sense
    result = http_status_to_exit_status(-1)
    assert result == ExitStatus.ERROR

    result = http_status_to_exit_status(0)
    assert result == ExitStatus.ERROR
