"""Parses an HTML file and returns the list of links found in the HTML file."""


import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class HTMLParser:
    def __init__(self, html_soup, options=None):
        self.html_soup = html_soup
        self.external_urls = []
        self.internal_urls = []

    def parse(self):
        """
        Parses the HTML file and returns the list of links found in the HTML file.
        """

        links = self.html_soup.find_all("a")
        for link in links:
            if link.has_attr("href"):
                url = link["href"]
                if url.startswith("http"):
                    self.external_urls.append(url)
                else:
                    self.internal_urls.append(url)

        return self.external_urls, self.internal_urls
