import pytest

import pyHtmlProofer

# options = {"log_level": "DEBUG", "ignore_files": ["tests/out/index.html"]}
options = {"log_level": "ERROR", "disable_external": True}


def test_file_not_found_error():
    """Tests if error is raised if file is not found."""

    with pytest.raises(FileNotFoundError) as e:
        pyHtmlProofer.file("tests/cases/1/not_found", options=options).check()

    assert e.errisinstance(FileNotFoundError)


def test_file_name_is_string():
    """Tests if error is raised if file name is not a string."""

    with pytest.raises(TypeError) as e:
        pyHtmlProofer.file(["tests/cases/1/not_found"], options=options).check()

    assert e.errisinstance(TypeError)


def test_directory_not_found_error():
    """Tests if error is raised if directory is not found."""

    with pytest.raises(FileNotFoundError) as e:
        pyHtmlProofer.directories(["tests/cases/1/not_found"], options=options).check()

    assert e.errisinstance(FileNotFoundError)


def test_directory_name_is_list():
    """Tests if error is raised if directory name is not a list."""

    with pytest.raises(TypeError) as e:
        pyHtmlProofer.directories("tests/cases/1/not_found", options=options).check()

    assert e.errisinstance(TypeError)
