"""
# --*-- coding: utf-8 --*--
# htmlproofer - A tool for validating external links in HTML files
"""
import uuid
import re

import glob
from bs4 import BeautifulSoup
import requests
import urllib3


URL_TIMEOUT = 10.0
URL_BOT_ID = f"Bot {uuid.uuid4()}"
URL_HEADERS = {"User-Agent": URL_BOT_ID}


class HTMLProofer:
    """
    Takes either a path or sitemap url and returns a list of all links in the HTML.
    """

    def __init__(self) -> None:
        self.links = set()
        self.images = set()

    def check_directory(self, path: str) -> None:
        """
        Checks a directory for all links in the HTML.
        """
        # check for filenames ending with .html using glob.glob
        for file in glob.iglob(path + "/**/*.html", recursive=True):
            self.check_file(file)

    def check_file(self, file_path):
        """
        Checks a HTML file for all external links in the HTML.
        TODO: Add a feature to check for internal links
        """
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html5lib")
            for link in soup.find_all("a"):
                if link.get("href").startswith("http"):
                    self.links.add(link.get("href"))
            for image in soup.find_all("img"):
                if image.get("src").startswith("http"):
                    self.images.add(image.get("src"))
