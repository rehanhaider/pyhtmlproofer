from pyHTMLProofer.Config import Config
from pyHTMLProofer.utils.Log import Log
from pyHTMLProofer.utils.SitemapParser import SitemapParser


class Runner:
    def __init__(self, source, options=None):
        self.source = source
        self.options = Config.generate_defaults(options)
        self.LOGGER = Log(log_level=options["log_level"]).LOGGER

        self.external_urls = ()
        self.internal_urls = ()
        self.failures = ()

    def run(self):
        """
        Runs the runner module. Checks for the type of request then then excutes the appropriate method.
        """
        if self.options["type"] == "file":
            print(f"Checking file from inside runner: {self.source}")
        elif self.options["type"] == "directory":
            print("Checking directory, I'm inside runner")
        elif self.options["type"] == "directories":
            print("Checking directories, I'm inside runner")
        elif self.options["type"] == "sitemap":
            self.internal_urls = SitemapParser(self.source, self.options).get_urls()
        else:
            raise TypeError("Invalid type")
