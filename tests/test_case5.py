import pyHTMLProofer

options = {"log_level": "ERROR"}


links = ["https://example.com", "https://cloudbytes.dev"]


def test_links():
    """Tests the check links function."""

    failures = pyHTMLProofer.links(links, options=options).check()

    assert len(failures) == 0
