import pytest

from httpie.output.ui import man_pages


@pytest.fixture(autouse=True)
def enable_man_pages(mocker):
    mocker.patch.object(man_pages, 'NO_MAN_PAGES', False)
    mocker.patch.object(man_pages, 'is_windows', False)


def test_is_available_on_windows(mocker):
    # see https://github.com/httpie/cli/issues/1898
    mocker.patch.object(man_pages, 'is_windows', True)
    run = mocker.patch.object(man_pages.subprocess, 'run')
    run.return_value.returncode = 0

    assert man_pages.is_available('http') is False
    run.assert_not_called()


def test_is_available_when_disabled(mocker):
    mocker.patch.object(man_pages, 'NO_MAN_PAGES', True)
    run = mocker.patch.object(man_pages.subprocess, 'run')

    assert man_pages.is_available('http') is False
    run.assert_not_called()


def test_is_available_when_man_page_exists(mocker):
    run = mocker.patch.object(man_pages.subprocess, 'run')
    run.return_value.returncode = 0

    assert man_pages.is_available('http') is True


def test_is_available_when_man_page_is_missing(mocker):
    run = mocker.patch.object(man_pages.subprocess, 'run')
    run.return_value.returncode = 1

    assert man_pages.is_available('http') is False


def test_is_available_when_man_is_not_installed(mocker):
    mocker.patch.object(man_pages.subprocess, 'run', side_effect=FileNotFoundError)

    assert man_pages.is_available('http') is False
