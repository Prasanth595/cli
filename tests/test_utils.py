from pathlib import Path

import pytest

from httpie.utils import LockFileError, open_with_lockfile


@pytest.mark.parametrize('filename', ['version_info.json', '\u00ff\u00ff\u00ff.json'])
def test_open_with_lockfile_unicode_path(tmp_path, monkeypatch, filename):
    monkeypatch.chdir(tmp_path)
    lock_dir = tmp_path / 'locks'
    lock_dir.mkdir()
    monkeypatch.setattr('httpie.utils.tempfile.gettempdir', lambda: str(lock_dir))
    target = Path(filename)

    with open_with_lockfile(target, 'w') as stream:
        stream.write('saved')
        assert len(list(lock_dir.iterdir())) == 1
        with pytest.raises(LockFileError):
            with open_with_lockfile(target, 'w'):
                pass

    assert target.read_text() == 'saved'
    assert list(lock_dir.iterdir()) == []
    with open_with_lockfile(target) as stream:
        assert stream.read() == 'saved'


def test_open_with_lockfile_releases_after_error(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    lock_dir = tmp_path / 'locks'
    lock_dir.mkdir()
    monkeypatch.setattr('httpie.utils.tempfile.gettempdir', lambda: str(lock_dir))

    with pytest.raises(ValueError, match='failed'):
        with open_with_lockfile(Path('\u00ff\u00ff\u00ff.json'), 'w'):
            raise ValueError('failed')

    assert list(lock_dir.iterdir()) == []
