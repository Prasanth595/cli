"""Miscellaneous regression tests"""
import pytest

from httpie.compat import is_windows
from .utils.matching import assert_output_matches, Expect
from .utils import HTTP_OK, MockEnvironment, http


def test_Host_header_overwrite(httpbin):
    """
    https://github.com/httpie/cli/issues/235

    """
    host = 'pie.dev'
    url = httpbin + '/get'
    r = http('--print=hH', url, f'host:{host}')
    assert HTTP_OK in r
    assert r.lower().count('host:') == 1
    assert f'host: {host}' in r


@pytest.mark.parametrize(
    'url, expected_host',
    [
        # Default ports must be stripped from the displayed Host
        # header to match what `http.client` actually sends on the
        # wire (it omits the port when it equals the scheme default).
        ('http://localhost:80/', 'localhost'),
        ('https://example.com:443/', 'example.com'),
        # Userinfo should not appear in Host either way.
        ('http://user:pass@localhost:80/', 'localhost'),
        # Non-default ports must be preserved.
        ('http://localhost:8080/', 'localhost:8080'),
        ('https://example.com:80/', 'example.com:80'),
        ('https://example.com:8443/', 'example.com:8443'),
        # No explicit port -> no port in Host.
        ('https://example.com/', 'example.com'),
        # IPv6 hosts keep their brackets.
        ('http://[::1]:80/', '[::1]'),
        ('http://[::1]:8080/', '[::1]:8080'),
    ],
)
def test_Host_header_default_port_stripped(url, expected_host):
    """
    https://github.com/httpie/cli/issues/1034
    """
    r = http('--offline', '--print=H', url)
    host_lines = [
        line for line in r.splitlines()
        if line.lower().startswith('host:')
    ]
    assert len(host_lines) == 1, r
    assert host_lines[0] == f'Host: {expected_host}', r


@pytest.mark.skipif(is_windows, reason='Unix-only')
def test_output_devnull(httpbin):
    """
    https://github.com/httpie/cli/issues/252

    """
    http('--output=/dev/null', httpbin + '/get')


def test_verbose_redirected_stdout_separator(httpbin):
    """

    <https://github.com/httpie/cli/issues/1006>
    """
    r = http(
        '-v',
        httpbin + '/post',
        'a=b',
        env=MockEnvironment(stdout_isatty=False),
    )
    assert '}HTTP/' not in r
    assert_output_matches(r, [
        Expect.REQUEST_HEADERS,
        Expect.BODY,
        Expect.SEPARATOR,
        Expect.RESPONSE_HEADERS,
        Expect.BODY,
    ])
