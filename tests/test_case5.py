import pyhtmlproofer

options = {"log_level": "ERROR"}


links = ["https://example.com", "https://cloudbytes.dev"]


def test_links():
    """Tests the check links function."""

    failures = pyhtmlproofer.links(links, options=options).check()

    assert len(failures) == 0
