import importlib


def test_app_imports():
    app_module = importlib.import_module("app.main")
    assert app_module.app is not None
