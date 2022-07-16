import pyHTMLProofer


def test_app():
    """Tests the app."""
    file_path = "tests/out/index.html"
    options = {"log_level": "DEBUG", "ignore_files": ["tests/out/index.html"]}
    options = {"log_level": "DEBUG", "disable_external": True}
    options = {"log_level": "ERROR", "disable_external": True}
    # pyHTMLProofer.file(file_path, options=options).check()
    pyHTMLProofer.directories(["/workspaces/pyhtmlproofer/tests/out"], options=options).check()
