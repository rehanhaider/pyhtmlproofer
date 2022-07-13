"""This class validates URLs format and segregates them into internal and external URLs."""
import requests
from bs4 import BeautifulSoup
from pyHTMLProofer.utils import HTMLParser


class _URL:
    def __init__(self, url, options=None, base_url=None):
        self.url = url
        self.options = options
        self.html_soup = None
        self.type = "external" if base_url else "internal"
        self.base_url = base_url

    def validate(self):
        """
        This method is used to validate URLs.
        """

        if self.type == "external":
            return self._validate_external_url()
        elif self.type == "internal":
            return self._validate_internal_url()

    def get_links(self):
        """
        This method is used to get links from the HTML file.
        """
        if not self.html_soup:
            self.validate()

        external_urls, internal_urls = HTMLParser(self.html_soup, options=self.options).get_links()

        return external_urls, internal_urls

    def _validate_external_url(self):
        """
        This method is used to validate external URLs.
        """
        try:
            response = requests.get(
                self.url,
                headers=self.options["HTTP"]["headers"],
                timeout=self.options["HTTP"]["timeout"],
                allow_redirects=self.options["HTTP"]["followlocation"],
            )
            if response.status_code != 200:
                return False
            self.html_soup = BeautifulSoup(response.text, "html5lib")
            return True
        except Exception:
            return False

    def _validate_internal_url(self):
        """
        This method is used to validate internal URLs.
        """
