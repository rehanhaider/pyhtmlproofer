from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Checker import Checker

from os import path

from bs4 import BeautifulSoup

from .HTML import HTML


class FILE:
    def __init__(self, checker: Checker) -> None:
        self.file_path = checker.current_url
        self.options = checker.options
        self.LOGGER = checker.LOGGER
        self.html_soup = None
        self.file_external_urls = {}
        self.file_internal_urls = {}

    def check(self):
        # Check if a file exists
        self.LOGGER.debug(f"Checking file: {self.file_path}")
        if not path.isfile(self.file_path):
            self.LOGGER.error(f"File does not exist: {self.file_path}")
        else:
            # If file exists, get the HTML soup
            self.LOGGER.debug(f"File exists: {self.file_path}")
            self.html_soup = self.get_html_soup()
            # Get the links from the HTML file
            self.LOGGER.debug(f"Getting links from HTML file: {self.file_path}")
            html = HTML(self.html_soup, options=self.options)
            file_external_urls, file_internal_urls = html.get_links()

            # Add the links to dictionary
            for url in file_external_urls:
                self.file_external_urls[url] = [self.file_path]

            for url in file_internal_urls:
                if url.startswith("#"):
                    url = self.file_path + url
                    self.LOGGER.debug(f"Internal reference found: {url}")
                # self.LOGGER.error(self.file_path)
                self.file_internal_urls[url] = [self.file_path]

        # Return empty lists if file doesn't exist
        return self.file_external_urls, self.file_internal_urls

    def get_html_soup(self):
        self.LOGGER.debug(f"Getting HTML Soup: {self.file_path}")
        with open(self.file_path, "r") as f:
            html_soup = BeautifulSoup(f.read(), "html5lib")
        return html_soup
