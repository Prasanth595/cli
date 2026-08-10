from unittest.mock import Mock

from httpie.output.ui import man_pages


def test_man_pages_are_unavailable_on_windows(monkeypatch):
    run = Mock()
    monkeypatch.setattr(man_pages.sys, 'platform', 'win32')
    monkeypatch.setattr(man_pages.subprocess, 'run', run)

    assert man_pages.is_available('http') is False
    run.assert_not_called()
