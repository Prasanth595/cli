def test_httpie_imports():
    import httpie
    import httpie.core
    import httpie.utils

    assert httpie is not None
    assert httpie.core is not None
    assert httpie.utils is not None