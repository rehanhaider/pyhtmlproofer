"""
A tool for validating internal & external links in HTML files / Websites
"""


from argparse import ArgumentError
import logging
import os


VERSION = "0.1.0.alpha"


class pyHTMLProofer:
    def __init__(self) -> None:
        self.VERSION = "0.1.0.alpha"

    def check_file(self, file_path):
        """
        Check the file for internal & external links
        :param file_path:
        :return:
        """
        # Raise error if file path is not a string
        if not isinstance(file_path, str):
            raise ArgumentError("File path must be a string")

        # Raise error if the file does not exist
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        print("Checking a single file")
        return True

    def check_directory(self, directory_path):
        """
        Check the directory for internal & external links
        :param directory_path:
        :return:
        """

        # Raise error if directory path is not a string
        if not isinstance(directory_path, str):
            raise ArgumentError("Directory path must be a string")

        # Raise error if the directory does not exist
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory does not exist: {directory_path}")

        print("Checking a single directory")
        return True

    def check_directories(self, directory_paths):
        """
        Check the directories for internal & external links
        :param directory_paths:
        :return:
        """

        # Raise error if directory path is not a string
        if not isinstance(directory_paths, list):
            raise ArgumentError("Directory paths must be a list")

        # Raise error if the directory does not exist
        for directory_path in directory_paths:
            if not os.path.isdir(directory_path):
                raise FileNotFoundError(f"Directory does not exist: {directory_path}")

        print("Checking list of directories")
        return True

    def check_links(self, links):
        """
        Check the links for internal & external links
        :param links:
        :return:
        """

        # Raise error if link is not a string
        if not isinstance(links, list):
            raise ArgumentError("Links must be a list")

        print("Checking list of Links")
        return True

    class Configuration:
        def __init__(self):

            self.DEFAULT_TESTS = ["Links", "Images", "Scripts"]

            self.PROOFER_DEFAULTS = {
                "allow_hash_href": True,
                "allow_missing_href": False,
                "assume_extension": ".html",
                "check_external_hash": True,
                "checks": self.DEFAULT_TESTS,
                "directory_index_file": "index.html",
                "disable_external": False,
                "ignore_empty_mailto": False,
                "ignore_files": [],
                "ignore_missing_alt": False,
                "ignore_status_codes": [],
                "ignore_urls": [],
                "enforce_https": True,
                "extensions": [".html"],
                "log_level": "info",
                "only_4xx": False,
                "swap_attributes": {},
                "swap_urls": {},
            }

            self.HTTP_DEFAULTS = {
                "followlocation": True,
                "headers": {
                    "User-Agent": f"Mozilla/5.0 (compatible; HTML Proofer/{pyHTMLProofer().VERSION}; https://github.com/rehanhaider/htmlproofer)",
                    "Accept": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
                },
                "connecttimeout": 10,
                "timeout": 10,
            }

            self.AIOHTTP_DEFAULTS = {
                "max_concurrency": 50,
            }

            self.PARALLEL_DEFAULTS = {"enabled": True}

            self.CACHE_DEFAULTS = {}

        def generate_defaults(self, opts=None):
            """
            Generate default configuration options
            :param opts:
            :return:
            """
            if opts is None:
                opts = {}

            options = self.PROOFER_DEFAULTS.copy()  # .update(opts)
            options.update(opts)

            options["HTTP"] = dict(self.HTTP_DEFAULTS, **options["HTTP"]) if "HTTP" in options else self.HTTP_DEFAULTS
            options["AIOHTTP"] = (
                dict(self.AIOHTTP_DEFAULTS, **options["AIOHTTP"]) if "AIOHTTP" in options else self.AIOHTTP_DEFAULTS
            )
            options["PARALLEL"] = (
                dict(self.PARALLEL_DEFAULTS, **options["PARALLEL"])
                if "PARALLEL" in options
                else self.PARALLEL_DEFAULTS
            )
            options["CACHE"] = (
                dict(self.CACHE_DEFAULTS, **options["CACHE"]) if "CACHE" in options else self.CACHE_DEFAULTS
            )

            return options

    class Log:
        import logging

        STDOUT_LEVELS = ("debug", "info", "warning")
        STDERR_LEVELS = ("error", "critical")

        def __init__(self, log_level):
            """Initialise Logger"""
            logging.basicConfig(level=log_level)
            self.logger = logging.getLogger("pyHTMLProofer")

        def log(self, message, level="info"):
            pass

        def log_with_color(self, message, level="info"):
            pass

        def colorize(self, message, level="info"):
            pass

    class Runner:

        URL_TYPES = ("internal", "external")

        def __init__(self, src, opts=None):
            self.options = pyHTMLProofer().Configuration().generate_defaults(opts)
            self.source = src

            logger = pyHTMLProofer().Log(pyHTMLProofer().Configuration().options["log_level"])
