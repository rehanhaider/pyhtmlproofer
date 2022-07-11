import pyHTMLProofer


def test_app():
    """Tests the app."""
    sitemap = "https://cloudbytes.dev/sitemap.xml"
    pyHTMLProofer.check_sitemap(sitemap, options={"log_level": "INFO"}).run()
