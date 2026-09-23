import pytest
from httpie.context import Environment

from .utils import MockEnvironment, http
from httpie.compat import is_windows


@pytest.mark.skipif(not is_windows, reason='windows-only')
class TestWindowsOnly:

    @pytest.mark.skipif(True,
                        reason='this test for some reason kills the process')
    def test_windows_colorized_output(self, httpbin):
        # Spits out the colorized output.
        http(httpbin + '/get', env=Environment())


def test_is_available_false_on_windows(monkeypatch):
    # Regression: os.system == 'nt' is always False (os.system is a function).
    from httpie.output.ui import man_pages

    monkeypatch.setattr(man_pages.os, 'name', 'nt')
    monkeypatch.setattr(man_pages, 'NO_MAN_PAGES', False)
    assert man_pages.is_available('http') is False


class TestFakeWindows:
    def test_output_file_pretty_not_allowed_on_windows(self, tmp_path, httpbin):
        env = MockEnvironment(is_windows=True)
        output_file = tmp_path / 'test_output_file_pretty_not_allowed_on_windows'
        r = http('--output', str(output_file),
                 '--pretty=all', 'GET', httpbin + '/get',
                 env=env, tolerate_error_exit_status=True)
        assert 'Only terminal output can be colorized on Windows' in r.stderr
