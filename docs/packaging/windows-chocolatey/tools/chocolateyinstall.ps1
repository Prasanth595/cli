$ErrorActionPreference = 'Stop';
python -m pip install $env:ChocolateyPackageName==$env:ChocolateyPackageVersion --disable-pip-version-check
