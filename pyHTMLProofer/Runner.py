from ast import Raise
from pyHTMLProofer.Config import Config
from pyHTMLProofer.utils.Log import Log


class Runner:
    def __init__(self, source, options=None):
        self.source = source
        self.options = Config.generate_defaults(options)
        self.LOGGER = Log(log_level=options["log_level"]).LOGGER

        self.external_urls = ()
        self.internal_urls = ()
        self.failures = ()

    def run(self):
        if self.options["type"] == "file":
            print(f"Checking file from inside runner: {self.source}")
        elif self.options["type"] == "directory":
            print("Checking directory, I'm inside runner")
        elif self.options["type"] == "directories":
            print("Checking directories, I'm inside runner")
        elif self.options["type"] == "sitemap":
            print("Checking sitemap, I'm inside runner")
        else:
            raise TypeError("Invalid type")
