# BUG-1 Root Cause Analysis

## Proximate

`setup.py` line 2 in httpie 0.1.3: `from httpie import httpie`. This caused `httpie/pretty.py` to be imported, which contained `import pygments` at module scope (line 3). pip runs `python setup.py egg_info` before installing any declared dependencies, so pygments was not yet available.

## Root

Mental model gap: the developer treated setup.py as an ordinary Python script that could import from the package being installed. In reality, setup.py is executed by the build system (pip/setuptools) in a bare environment where only stdlib and setuptools are guaranteed to be present. Importing from the package under installation pulls in its transitive runtime dependencies, violating the build-time vs. install-time dependency boundary.

## Systemic

The structural fix is the migration from a dynamic setup.py (with imports) to a purely declarative `setup.cfg` / `pyproject.toml` (PEP 517/518). This was completed in commit `10b7d31`. The regression test `tests/regressions/test_BUG-1_setup_pygments_import.py` locks in the invariant: executing setup.py must not trigger import of pygments or any other third-party runtime dependency. The test is chmod 444 and blocks any future regression at the CI gate level.
