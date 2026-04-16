import httpie
import httpie.core
import httpie.utils
import httpie.cli


def test_core_modules_import():
    # ensures core modules are importable
    assert httpie is not None
    assert httpie.core is not None
    assert httpie.utils is not None


def test_cli_module_import():
    # ensures CLI layer is correctly packaged
    assert httpie.cli is not None


def test_package_has_expected_attributes():
    # basic sanity check for package integrity
    assert hasattr(httpie, "__name__")
    assert httpie.__name__ == "httpie"