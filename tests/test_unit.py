import pyHTMLProofer
from pyHTMLProofer.validator.external import External


def test_external_url_validator():
    """Tests the external URL validator."""
    url = External("https://www.google.com")
    assert url.validate() is True


def test_check_file():
    """Tests the check file function."""
    file_path = "tests/out/test_dir1/test_file1.html"
    pyHTMLProofer.check_file(file_path, options={"log_level": "INFO"}).run()


def test_check_directory():
    """Tests the check directory function."""
    directory_path = "tests/out/test_dir1"
    pyHTMLProofer.check_directory(directory_path, options={"log_level": "INFO"}).run()


def test_check_directories():
    """Tests the check directories function."""
    directory_paths = ["tests/out/test_dir1", "tests/out"]
    pyHTMLProofer.check_directories(directory_paths, options={"log_level": "INFO"}).run()


def test_check_sitemap():
    """Tests the check sitemap function."""
    sitemap = "https://cloudbytes.dev/sitemap.xml"
    pyHTMLProofer.check_sitemap(sitemap, options={"log_level": "INFO"}).run()
