$ErrorActionPreference = 'Stop';
python -m pip uninstall -y $env:ChocolateyPackageName --disable-pip-version-check
