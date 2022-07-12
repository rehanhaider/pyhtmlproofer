import pyHTMLProofer
from pyHTMLProofer.validator.external import External


def test_external_url_validator():
    """Tests the external URL validator."""
    url = External("https://www.google.com")
    assert url.validate() is True


def test_links():
    """Tests the check links function."""
    directory_paths = ["https://www.google.com", "https://cloudbytes.dev/sitemap.xml"]
    pyHTMLProofer.check_links(directory_paths, options={"log_level": "INFO"}).run()


def test_check_sitemap():
    """Tests the check sitemap function."""
    sitemap = "https://cloudbytes.dev/sitemap.xml"
    pyHTMLProofer.check_sitemap(sitemap, options={"log_level": "INFO"}).run()
