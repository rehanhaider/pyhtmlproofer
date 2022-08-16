import pytest

import pyHtmlProofer

options = {"log_level": "ERROR", "disable_external": True}


files = ["tests/cases/1/file1.html", "tests/cases/1/file2.html", "tests/cases/1/file3.html"]


@pytest.mark.parametrize("file", files)
def test_file(file):
    """Tests the check links function."""

    failures = pyHtmlProofer.file(file, options=options).check()
    assert len(failures) == 0


def test_directory():
    """Tests the check links function."""
    directory_paths = ["tests/cases/1/"]
    failures = pyHtmlProofer.directories(directory_paths, options=options).check()

    assert len(failures) == 0
