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

LOCALHOST_PATTERNS = ("localhost", "127.0.0.1", "app_server")


class HTMLProofer:
    """
    Takes either a path or sitemap url and returns a list of all links in the HTML.
    """

    def __init__(self) -> None:
        self.links = set()

    def check_directory(self, path: str) -> None:
        """
        Checks a directory for all links in the HTML.
        """
        # check for filenames ending with .html using glob.glob
        for file in glob.iglob(path + "/**/*.html", recursive=True):
            self.check_file(file)
            for url in self.links:
                print(self.get_url_status(url))

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

    def get_url_status(self, url):
        for local in LOCALHOST_PATTERNS:
            if url.startswith("http://" + local):
                return (url, 0)
        clean_url = url.strip("?.")
        try:
            response = requests.get(clean_url, verify=False, timeout=URL_TIMEOUT, headers=URL_HEADERS)
            return (clean_url, response.status_code)
        except requests.exceptions.Timeout:
            return (clean_url, 504)
        except requests.exceptions.ConnectionError:
            return (clean_url, -1)
