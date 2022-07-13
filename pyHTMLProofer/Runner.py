from urllib.parse import urlparse
from pyHTMLProofer.Config import Config
from pyHTMLProofer.utils import Log
from pyHTMLProofer.utils import SitemapParser
from pyHTMLProofer.utils import HTMLParser
from pyHTMLProofer.utils import _URL


class Runner:
    def __init__(self, source, options=None):
        self.source = source
        self.options = Config.generate_defaults(options)
        self.LOGGER = Log(log_level=options["log_level"]).LOGGER
        self.external_urls = []
        self.internal_urls = []
        self.failures = []

    def run(self):
        """
        Runs the runner module. Checks for the type of request then then excutes the appropriate method.
        """
        if self.options["type"] == "links":
            print(f"Checking following links from inside runner: {self.source}")
            self.check_links()
        elif self.options["type"] == "sitemap":
            self.LOGGER.info(f"Checking for URLs in sitemap: {self.source}")
            self.check_site()
        else:
            raise TypeError("Invalid type")

    def check_site(self):
        """
        Checks the URLs listed in sitemap for internal & external links.
        """
        # EXtract the hostname from the URL

        self.LOGGER.info(f"Checking for URLs in sitemap: {self.source}")
        # Parse the sitemap.xml and fetch all unique URLs
        self.source = SitemapParser(self.source, self.options).get_urls()

        # Check the list of URLs found in the sitemap
        self.LOGGER.info("Checking URLs in sitemap")
        self.check_links()

    def check_links(self):  # sourcery skip: remove-unnecessary-else
        """
        Checks the internal & external links in the HTML to see if they're broken.
        """
        for url in self.source:
            base_url = f"{urlparse(self.source).scheme}:\\{urlparse(self.source).hostname}"
            URL = _URL(url, options=self.options, base_url=base_url)
            # Check if provided URL is valid or not by sending a GET request
            # TODO: Change the GET to HEAD request in future
            if URL.validate() is False:
                raise ValueError(f"URL is invalid: {url}")
            else:
                self.LOGGER.info(f"Finding links in {url}")
                external_urls, internal_urls = URL.get_links()
                # TODO: Check if the links are unique or not. If not add them to master list with metadata in dict format

                # TODO: Restart working from here

        # Check the list of external links
        self.LOGGER.info("Checking external links")
        for url in self.external_urls:
            self.LOGGER.info(f"Checking external link: {url}")
            URL = _URL(url, options=self.options)
            if URL.validate() is False:
                self.failures.append(url)
                self.LOGGER.error(f"URL is invalid: {url}")

        # Check the list of internal links
        self.LOGGER.info("Checking internal links")
        for url in self.internal_urls:
            self.LOGGER.info(f"Checking internal link: {url}")
            URL = _URL(
                url,
                options=self.options,
            )
            if URL.validate() is False:
                self.failures.append(url)
                self.LOGGER.error(f"URL is invalid: {url}")

    def get_links_from_url(self, html_soup):
        """
        Checks the internal or external link in the HTML to see if it's broken.
        """
        # Get all the links in the HTML
        external_urls, internal_urls = HTMLParser(html_soup, options=self.options).get_links()
