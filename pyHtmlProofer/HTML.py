"""Parses an HTML file and returns the list of links found in the HTML file."""

from bs4 import BeautifulSoup


class HTML:
    def __init__(self, html_soup: BeautifulSoup, options=None):
        self.html_soup = html_soup
        self.external_urls = []
        self.internal_urls = []

    def get_links(self):
        """
        Parses the HTML file and returns the list of links found in the HTML file.
        """

        links = self.html_soup.find_all("a")
        for link in links:
            if link.has_attr("href"):
                url = link["href"]
                if url.startswith("http"):
                    self.external_urls.append(url)
                elif url.startswith("//"):
                    url = f"https:{url}"
                    self.external_urls.append(url)
                else:
                    self.internal_urls.append(url)

        return self.external_urls, self.internal_urls

    def check_reference(self, internal_reference):
        # Check if the internal reference is a hyperlink in the HTML file
        if self.html_soup.find("a", href=internal_reference):
            return True
