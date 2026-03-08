from unittest import mock

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


class TestFakeWindows:
    def test_output_file_pretty_not_allowed_on_windows(self, tmp_path, httpbin):
        env = MockEnvironment(is_windows=True)
        output_file = tmp_path / 'test_output_file_pretty_not_allowed_on_windows'
        r = http('--output', str(output_file),
                 '--pretty=all', 'GET', httpbin + '/get',
                 env=env, tolerate_error_exit_status=True)
        assert 'Only terminal output can be colorized on Windows' in r.stderr

    def test_windows_piped_pretty_uses_raw_stream(self, httpbin):
        """When stdout is piped on Windows, write_stream() should be used
        instead of write_stream_with_colors_win() so ANSI codes pass
        through to pagers like `less -r`. Regression test for #799."""
        env = MockEnvironment(
            is_windows=True,
            stdout_isatty=False,
            colors=256,
        )
        with mock.patch('httpie.output.writer.write_stream') as write_stream, \
             mock.patch('httpie.output.writer.write_stream_with_colors_win') as write_colors_win:
            http('--pretty=all', 'GET', httpbin + '/get', env=env)
            write_stream.assert_called()
            write_colors_win.assert_not_called()
