from pathlib import Path

import pytest
from _pytest.monkeypatch import MonkeyPatch

from httpie.compat import is_windows
from httpie.encoding import UTF8
from httpie.config import (
    Config, DEFAULT_CONFIG_DIRNAME, DEFAULT_CONFIG_FILENAME,
    DEFAULT_LOCAL_CONFIG_DIRNAME, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR,
    DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_WINDOWS_CONFIG_DIR,
    ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME, find_local_config_dir,
    get_default_config_dir,
)
from .utils import HTTP_OK, MockEnvironment, http


def test_default_options(httpbin):
    env = MockEnvironment()
    env.config['default_options'] = ['--form']
    env.config.save()
    r = http(httpbin + '/post', 'foo=bar', env=env)
    assert r.json['form'] == {
        "foo": "bar"
    }


def test_config_file_not_valid(httpbin):
    env = MockEnvironment()
    env.create_temp_config_dir()
    (env.config_dir / Config.FILENAME).write_text('{invalid json}', encoding=UTF8)
    r = http(httpbin + '/get', env=env)
    assert HTTP_OK in r
    assert 'http: warning' in r.stderr
    assert 'invalid config file' in r.stderr


@pytest.mark.skipif(is_windows, reason='cannot chmod 000 on Windows')
def test_config_file_inaccessible(httpbin):
    env = MockEnvironment()
    env.create_temp_config_dir()
    config_path = env.config_dir / Config.FILENAME
    assert not config_path.exists()
    config_path.touch(0o000)
    assert config_path.exists()
    r = http(httpbin + '/get', env=env)
    assert HTTP_OK in r
    assert 'http: warning' in r.stderr
    assert 'cannot read config file' in r.stderr


def test_default_options_overwrite(httpbin):
    env = MockEnvironment()
    env.config['default_options'] = ['--form']
    env.config.save()
    r = http('--json', httpbin + '/post', 'foo=bar', env=env)
    assert r.json['json'] == {
        "foo": "bar"
    }


@pytest.mark.skipif(is_windows, reason='XDG_CONFIG_HOME needs *nix')
def test_explicit_xdg_config_home(monkeypatch: MonkeyPatch, tmp_path: Path):
    home_dir = tmp_path
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    monkeypatch.setenv('HOME', str(home_dir))
    custom_xdg_config_home = home_dir / 'custom_xdg_config_home'
    monkeypatch.setenv(ENV_XDG_CONFIG_HOME, str(custom_xdg_config_home))
    expected_config_dir = custom_xdg_config_home / DEFAULT_CONFIG_DIRNAME
    assert get_default_config_dir() == expected_config_dir


@pytest.mark.skipif(is_windows, reason='XDG_CONFIG_HOME needs *nix')
def test_default_xdg_config_home(monkeypatch: MonkeyPatch, tmp_path: Path):
    home_dir = tmp_path
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    monkeypatch.delenv(ENV_XDG_CONFIG_HOME, raising=False)
    monkeypatch.setenv('HOME', str(home_dir))
    expected_config_dir = (
        home_dir
        / DEFAULT_RELATIVE_XDG_CONFIG_HOME
        / DEFAULT_CONFIG_DIRNAME
    )
    assert get_default_config_dir() == expected_config_dir


@pytest.mark.skipif(is_windows, reason='legacy config dir needs *nix')
def test_legacy_config_dir(monkeypatch: MonkeyPatch, tmp_path: Path):
    home_dir = tmp_path
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    monkeypatch.setenv('HOME', str(home_dir))
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir()
    assert get_default_config_dir() == legacy_config_dir


def test_custom_config_dir(monkeypatch: MonkeyPatch, tmp_path: Path):
    httpie_config_dir = tmp_path / 'custom/directory'
    monkeypatch.setenv(ENV_HTTPIE_CONFIG_DIR, str(httpie_config_dir))
    assert get_default_config_dir() == httpie_config_dir


@pytest.mark.skipif(not is_windows, reason='windows-only')
def test_windows_config_dir(monkeypatch: MonkeyPatch):
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR


def make_local_config_dir(directory: Path) -> Path:
    local_config_dir = directory / DEFAULT_LOCAL_CONFIG_DIRNAME
    local_config_dir.mkdir(parents=True)
    (local_config_dir / DEFAULT_CONFIG_FILENAME).write_text('{}', encoding=UTF8)
    return local_config_dir


def test_local_config_dir_in_cwd(monkeypatch: MonkeyPatch, tmp_path: Path):
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    local_config_dir = make_local_config_dir(tmp_path)
    monkeypatch.chdir(tmp_path)
    assert get_default_config_dir() == local_config_dir


def test_local_config_dir_in_parent(monkeypatch: MonkeyPatch, tmp_path: Path):
    monkeypatch.delenv(ENV_HTTPIE_CONFIG_DIR, raising=False)
    local_config_dir = make_local_config_dir(tmp_path)
    nested_dir = tmp_path / 'deeply' / 'nested' / 'directory'
    nested_dir.mkdir(parents=True)
    monkeypatch.chdir(nested_dir)
    assert get_default_config_dir() == local_config_dir


def test_local_config_dir_nearest_match_wins(monkeypatch: MonkeyPatch, tmp_path: Path):
    make_local_config_dir(tmp_path)
    nested_dir = tmp_path / 'nested'
    nested_dir.mkdir()
    nested_config_dir = make_local_config_dir(nested_dir)
    assert find_local_config_dir(start_dir=nested_dir) == nested_config_dir


def test_local_config_dir_requires_config_file(monkeypatch: MonkeyPatch, tmp_path: Path):
    (tmp_path / DEFAULT_LOCAL_CONFIG_DIRNAME).mkdir()
    assert find_local_config_dir(start_dir=tmp_path) is None


def test_local_config_dir_ignored_when_env_config_dir_set(
    monkeypatch: MonkeyPatch, tmp_path: Path
):
    make_local_config_dir(tmp_path)
    monkeypatch.chdir(tmp_path)
    httpie_config_dir = tmp_path / 'custom/directory'
    monkeypatch.setenv(ENV_HTTPIE_CONFIG_DIR, str(httpie_config_dir))
    assert get_default_config_dir() == httpie_config_dir
