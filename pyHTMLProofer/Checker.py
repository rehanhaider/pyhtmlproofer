from optparse import Option
from time import sleep
from typing import Union, Dict, Optional, List, AnyStr
from os import path

from .Config import Config
from .Log import Log
from .FILE import FILE
from .Utils import merge_urls, crawl_directory
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

        self.current_url = ""

    def check(self) -> None:
        if self.type == "file":
            self.check_file(self.source)
        elif self.type == "directories":
            self.check_directories(self.source)

        self.validate()
        self.LOGGER.error(f"Failures: {self.failures}")

    def check_file(self, source: AnyStr, base_url: Optional[AnyStr] = None) -> None:
        # Raises an error if the file is not found.
        # This is specific to user provided file paths and not self-discovered ones
        # if not path.isfile(self.source):
        #    raise FileNotFoundError(f"File does not exist: {self.source}")
        if not base_url:  # Invoked in case of one file check otherwise set at global by the check_directories method
            self.base_url = path.dirname(path.abspath(source))  # Used for internal file paths
        self.LOGGER.debug(f"Base URL: {self.base_url}")
        self.current_url = source
        self.LOGGER.debug(f"Checking file: {source}")

        file_external_urls = {}
        file_internal_urls = {}

        if source in self.options["ignore_files"]:
            self.LOGGER.info(f"Ignoring file: {source}")
        # elif source in self.failures: #TODO: Needs to check the list of all values in the failures dict
        #     self.LOGGER.debug(f"File check already failed: {source}")
        else:
            self.LOGGER.debug("Initialising File Object...")
            file = FILE(self)
            file_external_urls, file_internal_urls = file.check()

        # self.LOGGER.error("External URLs: %s", file_external_urls)
        # self.LOGGER.error("Internal URLs: %s", file_internal_urls)

        self.external_urls = merge_urls(self.external_urls, file_external_urls)
        self.internal_urls = merge_urls(self.internal_urls, file_internal_urls)

    def check_directories(self, directories: List) -> None:
        """Checks all files in the directories provided.

        Args:
            directories (List): List of absolute paths to directories that needs to be checked
        """
        files = []
        for directory in directories:
            self.LOGGER.debug(f"Checking directory: {directory}")
            self.base_url = directory
            self.LOGGER.debug(f"Base URL: {self.base_url}")

            self.LOGGER.debug(f"Crawling Directory {directory}")
            files.extend(crawl_directory(directory))
            self.LOGGER.debug(f"Found {len(files)} files")

            # Remove duplicate files
            self.LOGGER.debug("Removing duplicate files")
            files = list(set(files))

            for file in files:
                self.check_file(file, self.base_url)

    def validate(self) -> None:
        self.validate_external_urls()
        self.validate_internal_urls()

    def validate_external_urls(self) -> None:
        if self.options["disable_external"]:
            self.LOGGER.info("External URL check disabled: Skipping")
            return

        for url in self.external_urls:
            if url in self.options["ignore_urls"]:
                self.LOGGER.info("Ignoring URL: %s", url)
            elif url in self.failures.values():
                self.LOGGER.debug("URL check already failed: %s", url)
            else:
                self.LOGGER.debug("Validating URL: %s", url)
                status = External(url, self.options).validate()
                if not status:
                    if self.current_url in self.failures.keys():
                        self.failures[self.current_url].append(url)
                    else:
                        self.failures[self.current_url] = [url]

    def validate_internal_urls(self) -> None:

        for url, sources in self.internal_urls.items():
            self.LOGGER.debug(f"Checking internal URL: {url}")
            if url in self.options["ignore_urls"]:
                self.LOGGER.info(f"Ignoring URL: {url}")
            elif url in self.failures.values():
                self.LOGGER.debug(f"URL check already failed: {url}")
            else:
                self.LOGGER.debug(f"Validating URL: {url}")
                if Internal(url, LOGGER=self.LOGGER, options=self.options, base_url=self.base_url).validate():
                    self.LOGGER.info(f"Found URL: {url}")
                else:
                    self.LOGGER.error(f"URL missing: {url}")
                    self.insert_failure(url, sources)

    def get_urls(self) -> Dict[AnyStr, List]:
        return self.external_urls, self.internal_urls

    def get_failures(self) -> List:
        return self.failures

    def insert_failure(self, url: AnyStr, sources: List) -> None:
        for source in sources:
            if source in self.failures.keys():
                self.failures[source].append(url)
            else:
                self.failures[source] = [url]