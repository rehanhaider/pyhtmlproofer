"""This module parses the sitemap and returns a list of URLs."""


from argparse import ArgumentError
import requests
from bs4 import BeautifulSoup


class SitemapParser:
    """This class is used to parse the sitemap and return a list of URLs."""

    def __init__(self, sitemap_url, options=None):
        self.sitemap_url = sitemap_url
        self.options = options

    def get_urls(self):
        """Generate the list of unique URLs in the sitemap.

        Raises:
            ArgumentError: The 
            FileNotFoundError: _description_

        Returns:
            _type_: _description_
        """

        # Raise error if sitemap URL is not a string
        if not isinstance(self.sitemap_url, str):
            raise ArgumentError("Sitemap URL must be a string")

        # Raise error if the sitemap does not exist
        if requests.get(self.sitemap_url).status_code != 200:
            raise FileNotFoundError(f"Sitemap does not exist: {self.sitemap_url}")

        # Parse the sitemap.xml and fetch all URLs
        response = requests.get(self.sitemap_url)
        soup = BeautifulSoup(response.text, features="xml")  # Uses "lxml", no need to specify

        # Return the unique list of URLs in sitemap
        return list({url.text for url in soup.find_all("loc")})
