---
bug_id: 1
closed_at: 2026-04-27
fix_sha: PENDING
root_class: mental-model
file_path: setup.py
symbol: setup
service: 
---
# BUG-1 Lesson

**Symptom**: ImportError: No module named pygments
**Root**: Mental model gap: the developer treated setup.py as an ordinary Python script that could import from the package being installed. In reality, setup.py is executed by the build system (pip/setuptools) in a bare environment where only stdlib and setuptools are guaranteed to be present. Importing from 
**Systemic**: The structural fix is the migration from a dynamic setup.py (with imports) to a purely declarative `setup.cfg` / `pyproject.toml` (PEP 517/518). This was completed in commit `10b7d31`. The regression test `tests/regressions/test_BUG-1_setup_pygments_import.py` locks in the invariant: executing setup
**Regression**: tests/regressions/test_BUG-1_setup_pygments_import.py
