import glob

import pytest
from bs4 import BeautifulSoup

import pyHtmlProofer
from pyHtmlProofer import Checker

options = {"log_level": "ERROR"}


def test_external_links():
    """Tests the external links function discovered from a file."""

    file_path = ["tests/cases/3/"]
    failures = pyHtmlProofer.directories(file_path, options=options).check()

    assert len(failures) == 0


# Check the number of links discovered in the directory
def test_directory_links_count():
    """Tests the check links function."""
    directory_paths = ["tests/cases/3/"]
    options["type"] = "directories"
    checker = Checker(directory_paths, options=options)

    checker.check()

    assert get_links_count(directory_paths[0]) == len(checker.external_urls.keys())


def get_links_count(directory_path):
    """Finds all the links in a directory."""

    links = []
    for file in glob.glob(f"{directory_path}/**/*.html", recursive=True):
        with open(file, "r") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            links.extend(link.get("href") for link in soup.find_all("a"))
    return len(set(links))
