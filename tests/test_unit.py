from pyHTMLProofer.validator.url import URL


def test_external_url_validator():
    """Tests the external URL validator."""
    url = URL("https://www.google.com")
    assert url.validate() is True



    