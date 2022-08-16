"""Parses an HTML file and returns the list of links found in the HTML file."""

from typing import AnyStr

from bs4 import BeautifulSoup


class HTML:
    def __init__(self, html_soup: BeautifulSoup, options=None):
        self.html_soup = html_soup
        self.external_urls = []
        self.internal_urls = []
        self.options = options

    def get_links(self):
        """
        Parses the HTML file and returns the list of links found in the HTML file.
        """
        hyperlinks = self.html_soup.find_all("a")
        self.extract_links(hyperlinks, "href")

        if "Links" in self.options["checks"]:
            links = self.html_soup.find_all("link")
            self.extract_links(links, "href")

        if "Images" in self.options["checks"]:
            images = self.html_soup.find_all("img")
            self.extract_links(images, "src")

        if "Scripts" in self.options["checks"]:
            scripts = self.html_soup.find_all("script")
            self.extract_links(scripts, "src")

        return self.external_urls, self.internal_urls

    def check_reference(self, internal_reference):
        # Check if the internal reference is a hyperlink in the HTML file
        if self.html_soup.find("a", href=internal_reference):
            return True

    def extract_links(self, links: BeautifulSoup, attr: AnyStr):
        """
        Extracts the links from the given BeautifulSoup object.
        """
        for link in links:
            if link.has_attr(attr):
                url = link[attr]
                if url.startswith("http"):
                    self.external_urls.append(url)
                elif url.startswith("//"):
                    url = f"https:{url}"
                    self.external_urls.append(url)
                else:
                    self.internal_urls.append(url)
