"""Tests for functions in `httpie.utils`."""
import pytest

from httpie.utils import is_version_greater


@pytest.mark.parametrize(
    'version_1, version_2, expected',
    [
        # Equal versions are not greater.
        ('1.0.0', '1.0.0', False),
        # Differences in each component are detected.
        ('1.0.1', '1.0.0', True),
        ('1.0.0', '1.0.1', False),
        ('1.1.0', '1.0.9', True),
        ('2.0.0', '1.9.9', True),
        # Components are compared numerically, not as strings
        # (a string comparison would wrongly consider '10' < '2').
        ('10.0.0', '2.0.0', True),
        ('2.0.0', '10.0.0', False),
        # A shorter version is smaller than a longer one sharing its prefix.
        ('1.0', '1.0.0', False),
        # Non-numeric suffixes are ignored, so a pre-release compares
        # as equal to its final release (and is therefore not greater).
        ('3.2.0-dev', '3.2.0', False),
        ('3.2.0', '3.2.0-dev', True),
    ]
)
def test_is_version_greater(version_1, version_2, expected):
    assert is_version_greater(version_1, version_2) is expected
