

def test_is_available_windows_guard_uses_sys_platform():
    from httpie.output.ui.man_pages import is_available
    import sys
    assert sys.platform != 'win32' or is_available('man') == False
