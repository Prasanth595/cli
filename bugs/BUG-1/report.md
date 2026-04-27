# BUG-1 Report

**Symptom**: ImportError: No module named pygments
**Ticket**: https://github.com/httpie/cli/issues/1
**Labels**: ["bug"]
**Repro Hint**: `sudo pip install httpie` fails during `python setup.py egg_info` because setup.py executed `from httpie import httpie` which imported `httpie/pretty.py` which did `import pygments` at module scope, before pip had installed pygments.
**Env**: Ubuntu 11.10, httpie 0.1.3, pip
**Target Symbol**: setup in setup.py
**Impact Summary**: Package installation failed when pygments was not pre-installed; fixed by removing httpie package imports from setup.py and migrating to declarative setup.cfg
