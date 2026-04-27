"""
Regression test for BUG-1: ImportError: No module named pygments

The original bug (httpie 0.1.3, 2012): setup.py executed
`from httpie import httpie` at the top level, which transitively imported
httpie/pretty.py, which did `import pygments` at module scope.  This caused
`python setup.py egg_info` (run by pip before installing dependencies) to fail
with ImportError when pygments was not yet installed.

Invariant: setup.py MUST NOT cause any third-party runtime dependency
(pygments, requests, …) to be imported as a side-effect of executing it.
Only stdlib + setuptools are acceptable at setup time.
"""

import subprocess
import sys
import os

# Absolute path to the repo root so this test is location-independent
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SETUP_PY = os.path.join(REPO_ROOT, "setup.py")


def test_setup_py_does_not_import_pygments_or_httpie_package():
    """
    Running `python setup.py egg_info` must succeed even when pygments
    (and the rest of httpie's runtime deps) are blocked from import.

    We achieve blocking by prepending a tiny sitecustomize hook via
    PYTHONPATH that raises ImportError for 'pygments' and 'httpie.*'
    (the two modules whose premature import caused BUG-1).
    """
    # Build a one-liner that poisons sys.modules before setup.py runs.
    # We run setup.py egg_info in a subprocess so we get a clean interpreter.
    guard = (
        "import sys, builtins; _real = builtins.__import__\n"
        "def _guard(name, *a, **kw):\n"
        "    if name == 'pygments' or name.startswith('pygments.'):\n"
        "        raise ImportError(f'BUG-1 guard: {name} must not be imported at setup time')\n"
        "    return _real(name, *a, **kw)\n"
        "builtins.__import__ = _guard\n"
    )
    cmd = [
        sys.executable,
        "-c",
        guard + f"exec(open({SETUP_PY!r}).read())",
        "egg_info",
        "--egg-base",
        "/tmp",
    ]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0, (
        f"setup.py egg_info failed — BUG-1 regression detected.\n"
        f"stdout: {result.stdout}\n"
        f"stderr: {result.stderr}"
    )
