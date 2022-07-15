from typing import Union, Dict, Optional, List, AnyStr
from os import path

from requests.api import options

# from wsgiref import validate
from .Config import Config
from .Log import Log
from .FILE import FILE
from .Utils import merge_urls
from .URL import External, Internal


class Checker:
    """
    `Checker` class is used to check the input files, links, or directories.
    """

    URL_TYPES = ("external", "internal")

    def __init__(self, source: Union[AnyStr, List], options: Optional[Dict] = None) -> None:
        self.options = Config.generate_defaults(options)
        self.type = self.options.pop("type")
        self.source = source

        self.LOGGER = Log(log_level=options["log_level"]).LOGGER

        # Initialise empty dictionaries
        # URL dict format is {url: [source1, source2, ...]}
        self.external_urls = {}
        self.internal_urls = {}

        # Initialise empty list
        # The format is {file_paths: [url1, url2, ...]}
        self.failures = {}

    def check(self) -> None:
        if self.type == "file":
            self.check_file()

        self.validate()
        self.LOGGER.info("Failures: %s", self.failures)

    def check_file(self) -> None:
        # Raises an error if the file is not found.
        # This is specific to user provided file paths and not self-discovered ones
        # if not path.isfile(self.source):
        #    raise FileNotFoundError(f"File does not exist: {self.source}")
        file_external_urls = {}
        file_internal_urls = {}

        if self.source in self.options["ignore_files"]:
            self.LOGGER.debug("Ignoring file: {self.source}")
        elif self.source in self.failures:
            self.LOGGER.debug("File check already failed: {self.source}")
        else:
            self.LOGGER.debug("Initialising File Object: {self.source}")
            file = FILE(self)
            file_external_urls, file_internal_urls = file.check()

        # self.LOGGER.info("External URLs: %s", file_external_urls)
        # self.LOGGER.info("Internal URLs: %s", file_internal_urls)

        self.external_urls = merge_urls(self.external_urls, file_external_urls)
        self.internal_urls = merge_urls(self.internal_urls, file_internal_urls)

        self.LOGGER.info("External URLs: %s", file_external_urls)

    def validate(self) -> None:
        self.validate_external_urls()
        self.validate_internal_urls()

    def validate_external_urls(self) -> None:
        if self.options["disable_external"]:
            self.LOGGER.debug("External URL check disabled: Skipping")
            return

        for url in self.external_urls:
            if url in self.options["ignore_urls"]:
                self.LOGGER.debug("Ignoring URL: %s", url)
            elif url in self.failures.values():
                self.LOGGER.debug("URL check already failed: %s", url)
            else:
                self.LOGGER.debug("Validating URL: %s", url)
                status = External(url, self.options).validate()
                if not status:
                    if self.source in self.failures.keys():
                        self.failures[self.source].append(url)
                    else:
                        self.failures[self.source] = [url]

    def validate_internal_urls(self) -> None:
        pass

    def get_urls(self) -> Dict[AnyStr, List]:
        return self.external_urls, self.internal_urls

    def get_failures(self) -> List:
        return self.failures
