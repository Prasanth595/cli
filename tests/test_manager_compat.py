from unittest.mock import Mock

from httpie.manager import compat


def test_discover_system_pip_falls_back_to_pip3(monkeypatch):
    # Arrange
    def which(name):
        return {
            "pip": None,
            "pip3": "/usr/local/bin/pip3",
        }[name]

    check_output = Mock(
        return_value="pip 23.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)"
    )

    monkeypatch.setattr(compat.shutil, "which", which)
    monkeypatch.setattr(compat.subprocess, "check_output", check_output)

    # Act
    pip = compat._discover_system_pip()

    # Assert
    assert pip == "/usr/local/bin/pip3"
    check_output.assert_called_once_with(
        ["/usr/local/bin/pip3", "--version"], text=True
    )


def test_discover_system_pip_skips_python2_pip(monkeypatch):
    # Arrange
    def which(name):
        return {
            "pip": "/usr/local/bin/pip",
            "pip3": "/usr/local/bin/pip3",
        }[name]

    def fake_check_output(cmd, text=True):
        if cmd[0] == "/usr/local/bin/pip":
            return (
                "pip 20.3 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)"
            )
        if cmd[0] == "/usr/local/bin/pip3":
            return "pip 23.0 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)"
        raise AssertionError(f"Unexpected executable passed to check_output: {cmd}")

    monkeypatch.setattr(compat.shutil, "which", which)
    monkeypatch.setattr(compat.subprocess, "check_output", fake_check_output)

    # Act
    pip = compat._discover_system_pip()

    # Assert
    assert pip == "/usr/local/bin/pip3"
