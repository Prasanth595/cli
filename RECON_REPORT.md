# RECON_REPORT

**Path:** `C:\httpie-assade-demo`  
**Duration:** 1533 ms

## Summary

Repo at `C:\httpie-assade-demo` contains 265 files (135 source, 107 test-related) across 5 directory levels (2074.6 KB total). Circular import detected (2 cycle(s)). Test coverage: 429 test functions across 35 test files (ratio 0.43). Documentation coverage is low (17%). Dominant tier: `at`.

## Scout

- Files: 265 (2074.6 KB)
- Source files: 135
- Max depth: 5
- Top-level: .editorconfig, .github, .gitignore, .packit.yaml, AUTHORS.md, CHANGELOG.md, CODE_OF_CONDUCT.md, CONTRIBUTING.md, LICENSE, MANIFEST.in

**By extension:**
  - `.py`: 133
  - `.json`: 26
  - `.md`: 24
  - `.xml`: 24
  - `.yml`: 17
  - `[no_ext]`: 8
  - `.sh`: 3
  - `.1`: 3

## Dependencies

- Python files: 133
- Unique external deps: 76
- Max import depth: 2
- Circular deps: YES — ['httpie/client.py → httpie/context.py → httpie/output/utils.py → httpie/output/utils.py', 'httpie/output/formatters/xml.py → httpie/output/formatters/xml.py']

## Tier Distribution

- `qk`: 6 — e.g. httpie/__init__.py, httpie/cli/nested_json/__init__.py
- `at`: 82 — e.g. setup.py, extras/packaging/linux/scripts/httpie_cli.py
- `mo`: 11 — e.g. httpie/context.py, httpie/cli/argparser.py
- `og`: 16 — e.g. httpie/compat.py, httpie/config.py
- `sy`: 18 — e.g. docs/contributors/fetch.py, docs/contributors/generate.py

**Violations:**
  - httpie/cli/definition.py (at, 29KB — may span tiers)
  - tests/test_output.py (at, 20KB — may span tiers)
  - tests/test_sessions.py (at, 27KB — may span tiers)

## Tests

- Test files: 35
- Test functions: 429
- Coverage ratio: 0.43
- Frameworks: pytest, unittest
- Untested modules: 66

**Untested (sample):**
  - `setup.py`
  - `docs/contributors/fetch.py`
  - `docs/contributors/generate.py`
  - `docs/installation/generate.py`
  - `extras/packaging/linux/build.py`
  - `extras/packaging/linux/scripts/http_cli.py`
  - `extras/packaging/linux/scripts/hooks/hook-pip.py`
  - `extras/profiling/benchmarks.py`

## Documentation

- README: yes
- Doc files: 26
- Public callables: 1107
- Documented: 189 (17%)

**Missing docstrings (sample):**
  - `docs/contributors/fetch.py:main`
  - `docs/contributors/fetch.py:find_committers`
  - `docs/contributors/fetch.py:find_reporters`
  - `docs/contributors/fetch.py:release_date`
  - `docs/contributors/fetch.py:load_awesome_people`
  - `docs/contributors/fetch.py:fetch`
  - `docs/contributors/fetch.py:new_person`
  - `docs/contributors/fetch.py:user`
  - `docs/contributors/fetch.py:fetch_missing_users_details`
  - `docs/contributors/fetch.py:save_awesome_people`

## Recommendations

1. Resolve 2 circular import(s) — introduce an interface layer or inversion-of-control.
2. Docstring coverage is 17%. Add docstrings to public functions and classes.
3. 3 file(s) may span tier boundaries. Split into smaller, single-purpose modules.

**Next action:** Fix circular imports first, then increase test coverage.
