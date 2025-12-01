import pytest
from httpie.cli.requestitems import RequestItems
from httpie.cli.argtypes import KeyValueArg
from httpie.cli.constants import SEPARATOR_HEADER_EMBED
from httpie.cli.exceptions import ParseError


def load_request_items(file_name: str):
    """Helper to create RequestItems from a header file."""
    arg = KeyValueArg(
        key=None,
        value=file_name,
        sep=SEPARATOR_HEADER_EMBED,
        orig=f"@{file_name}"
    )
    return RequestItems.from_args([arg])


def test_headers_txt():
    req_items = load_request_items('headers.txt')
    expected = {
        "X-API-Key": "12345",
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json",
    }
    for k, v in expected.items():
        assert req_items.headers.get(k) == v


def test_headers_with_empty_lines_txt():
    req_items = load_request_items('headers_with_empty_lines.txt')
    expected = {
        "X-API-Key": "12345",
        "User-Agent": "MyApp/1.0",
        "Accept": "application/json",
    }
    for k, v in expected.items():
        assert req_items.headers.get(k) == v


def test_headers_malformed_txt():
    # This file intentionally has a malformed header; should raise ParseError
    with pytest.raises(ParseError):
        load_request_items('headers_malformed.txt')
