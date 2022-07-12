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
            self.check_site()
        else:
            raise TypeError("Invalid type")

    def check_links(self):
        """
        Checks the internal & external links in the HTML to see if they're broken.
        """
        for url in self.source:
            URL = _URL(url, options=self.options)
            if URL.validate() is False:
                self.failures.append(url)
            else:
                self.get_links(URL.html_soup)

    def get_links(self, html_soup):
        """
        Checks the internal or external link in the HTML to see if it's broken.
        """
        external_urls, internal_urls = HTMLParser(html_soup, options=self.options).parse()
        self.LOGGER.info(f"External URLs: \n{external_urls}")
        self.LOGGER.info(f"Internal URLs: \n{internal_urls}")

        # self.external_urls.extend(external_urls)
        # self.internal_urls.extend(internal_urls)

    def check_site(self):
        """
        Checks the URLs listed in sitemap for internal & external links.
        """
        self.LOGGER.info(f"Checking for URLs in sitemap: {self.source}")
        # Parse the sitemap.xml and fetch all unique URLs
        self.source = SitemapParser(self.source, self.options).get_urls()

        # Check the list of URLs found in the sitemap
        self.LOGGER.info("Checking URLs in sitemap")
        self.check_links()
