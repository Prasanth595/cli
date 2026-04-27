# IMPORTANT: Do NOT import from the `httpie` package here.
# setup.py is executed by pip BEFORE dependencies are installed.
# Any import of httpie.* would pull in third-party deps (e.g. pygments)
# that are not yet available, causing InstallError.  See BUG-1.
# All metadata lives in setup.cfg (PEP 517/518 declarative style).
from setuptools import setup

setup()
