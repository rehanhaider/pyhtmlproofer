import pyHTMLProofer


def test_app():
    """Tests the app."""
    file_path = "tests/out/index.html"
    options = {"log_level": "DEBUG", "ignore_files": ["tests/out/index.html"]}
    options = {"log_level": "DEBUG"}
    pyHTMLProofer.file(file_path, options=options).check()
