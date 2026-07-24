import json
import os
from pathlib import Path
from typing import Any, Dict, Optional, Union

from . import __version__
from .compat import is_windows
from .encoding import UTF8


ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
ENV_HTTPIE_CONFIG_DIR = 'HTTPIE_CONFIG_DIR'
DEFAULT_CONFIG_DIRNAME = 'httpie'
DEFAULT_CONFIG_FILENAME = 'config.json'
DEFAULT_RELATIVE_XDG_CONFIG_HOME = Path('.config')
DEFAULT_RELATIVE_LEGACY_CONFIG_DIR = Path('.httpie')
DEFAULT_LOCAL_CONFIG_DIRNAME = '.httpie'
DEFAULT_WINDOWS_CONFIG_DIR = Path(
    os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME


def find_local_config_dir(start_dir: Optional[Path] = None) -> Optional[Path]:
    """
    Return the path to a local (per-project) configuration directory,
    or None if there isn’t one.

    Look for a `.httpie` directory containing a `config.json` file
    in `start_dir` (defaults to the current working directory) and,
    recursively, in its parents. The nearest match wins.

    The `config.json` file is required so that unrelated `.httpie`
    directories don’t accidentally become the active configuration
    directory.

    """
    try:
        current_dir = (start_dir or Path.cwd()).resolve()
    except OSError:
        return None
    for directory in (current_dir, *current_dir.parents):
        candidate = directory / DEFAULT_LOCAL_CONFIG_DIRNAME
        if (candidate / DEFAULT_CONFIG_FILENAME).is_file():
            return candidate
    return None


def get_default_config_dir() -> Path:
    """
    Return the path to the httpie configuration directory.

    This directory isn't guaranteed to exist, and nor are any of its
    ancestors (only the legacy ~/.httpie, if returned, is guaranteed to exist).

    XDG Base Directory Specification support:

        <https://wiki.archlinux.org/index.php/XDG_Base_Directory>

        $XDG_CONFIG_HOME is supported; $XDG_CONFIG_DIRS is not

    """
    # 1. explicitly set through env
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    if env_config_dir:
        return Path(env_config_dir)

    # 2. local per-project directory (a `.httpie/config.json` found
    #    in the current working directory or one of its parents)
    local_config_dir = find_local_config_dir()
    if local_config_dir:
        return local_config_dir

    # 3. Windows
    if is_windows:
        return DEFAULT_WINDOWS_CONFIG_DIR

    home_dir = Path.home()

    # 4. legacy ~/.httpie
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    if legacy_config_dir.exists():
        return legacy_config_dir

    # 5. XDG
    xdg_config_home_dir = os.environ.get(
        ENV_XDG_CONFIG_HOME,  # 5.1. explicit
        home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME  # 5.2. default
    )
    return Path(xdg_config_home_dir) / DEFAULT_CONFIG_DIRNAME


DEFAULT_CONFIG_DIR = get_default_config_dir()


class ConfigFileError(Exception):
    pass


def read_raw_config(config_type: str, path: Path) -> Dict[str, Any]:
    try:
        with path.open(encoding=UTF8) as f:
            try:
                return json.load(f)
            except ValueError as e:
                raise ConfigFileError(
                    f'invalid {config_type} file: {e} [{path}]'
                )
    except FileNotFoundError:
        pass
    except OSError as e:
        raise ConfigFileError(f'cannot read {config_type} file: {e}')


class BaseConfigDict(dict):
    name = None
    helpurl = None
    about = None

    def __init__(self, path: Path):
        super().__init__()
        self.path = path

    def ensure_directory(self):
        self.path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)

    def is_new(self) -> bool:
        return not self.path.exists()

    def pre_process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Hook for processing the incoming config data."""
        return data

    def post_process_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Hook for processing the outgoing config data."""
        return data

    def load(self):
        config_type = type(self).__name__.lower()
        data = read_raw_config(config_type, self.path)
        if data is not None:
            data = self.pre_process_data(data)
            self.update(data)

    def save(self, *, bump_version: bool = False):
        self.setdefault('__meta__', {})
        if bump_version or 'httpie' not in self['__meta__']:
            self['__meta__']['httpie'] = __version__
        if self.helpurl:
            self['__meta__']['help'] = self.helpurl

        if self.about:
            self['__meta__']['about'] = self.about

        self.ensure_directory()

        json_string = json.dumps(
            obj=self.post_process_data(self),
            indent=4,
            sort_keys=True,
            ensure_ascii=True,
        )
        self.path.write_text(json_string + '\n', encoding=UTF8)

    @property
    def version(self):
        return self.get(
            '__meta__', {}
        ).get('httpie', __version__)


class Config(BaseConfigDict):
    FILENAME = DEFAULT_CONFIG_FILENAME
    DEFAULTS = {
        'default_options': []
    }

    def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
        self.directory = Path(directory)
        super().__init__(path=self.directory / self.FILENAME)
        self.update(self.DEFAULTS)

    @property
    def default_options(self) -> list:
        return self['default_options']

    def _configured_path(self, config_option: str, default: str) -> None:
        return Path(
            self.get(config_option, self.directory / default)
        ).expanduser().resolve()

    @property
    def plugins_dir(self) -> Path:
        return self._configured_path('plugins_dir', 'plugins')

    @property
    def version_info_file(self) -> Path:
        return self._configured_path('version_info_file', 'version_info.json')

    @property
    def developer_mode(self) -> bool:
        """This is a special setting for the development environment. It is
        different from the --debug mode in the terms that it might change
        the behavior for certain parameters (e.g updater system) that
        we usually ignore."""

        return self.get('developer_mode')
