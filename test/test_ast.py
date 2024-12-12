from clean_imports.imports import get_imports


def test_ast():
    imports = list(get_imports(__file__))

    assert imports == ["clean_imports.imports.get_imports"]
