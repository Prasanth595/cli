# BUG-1 Journal

## Blast radius

The bug affected the `setup.py` entry point and transitively:
- `httpie/httpie.py` (now removed) — was imported in the original setup.py
- `httpie/pretty.py` (now removed) — was imported from httpie.py at module scope
- `pygments` — top-level import in pretty.py caused InstallError during `pip install`

In current code:
- `setup.py` is a 3-line stub: `from setuptools import setup; setup()`
- `httpie/pretty.py` no longer exists; formatting moved to `httpie/output/formatters/colors.py`
- `httpie/output/formatters/colors.py` imports pygments at module scope (line 3-16), but this file is only imported at runtime, never during package installation/metadata extraction.

## Structural hits

`ast-grep` for `from httpie import` in setup.py: none found (setup.py is a 3-line stub).
`ast-grep` for `import pygments` at module level in `httpie/output/formatters/colors.py`: found — lines 3-16. This is fine because the file is not reachable from setup.py.

## Skeleton view

Repo layout relevant to the bug:
- `setup.py` — 3 lines, no httpie imports
- `setup.cfg` — declares `Pygments>=2.5.2` in `install_requires` (correct approach)
- `httpie/output/formatters/colors.py` — imports pygments at module top, but only reachable after install

## Suspects

1. **[HISTORICAL — CONFIRMED]** `setup.py:2` executed `from httpie import httpie`, importing `httpie/pretty.py` which had `import pygments` at line 3. Mechanism: pip runs `python setup.py egg_info` before installing dependencies; the import chain triggered the missing-module error. Confirmed by issue traceback.

2. No current suspects — bug is already fixed.

## Archaeology

Key fix commits:
- Commit `10b7d31` (2024-03-18): "Migrate setup.py to setup.cfg (#1553)" — reduced setup.py to a 3-line stub with no httpie package imports, and moved all metadata to setup.cfg using PEP 517/518 standards.
- Historical: `httpie/pretty.py` was removed as part of output-pipeline refactoring (commit series around `ff6f188` "UI Enhancements").
