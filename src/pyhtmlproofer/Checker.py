from os import path
from typing import AnyStr, Dict, List, Optional, Union

from .Config import Config
from .FILE import FILE
from .Log import Log
from .Reporter import Reporter
from .URL import External, Internal
from .Utils import crawl_directory, merge_urls


class Checker:
    """
    `Checker` class is used to check the input files, links, or directories.
    """

    URL_TYPES = ("external", "internal")

    def __init__(self, source: Union[AnyStr, List], options: Optional[Dict] = None) -> None:
        self.options = Config.generate_defaults(options)
        self.type = self.options.pop("type")
        self.source = source

        self.LOGGER = Log(log_level=self.options["log_level"]).LOGGER

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
        elif self.type == "links":
            for link in self.source:
                self.check_link(link)
            # Checks the links and not crawls them for external URLs
            return self.failures

        else:
            raise ValueError(f"Invalid type: {self.type}")

        self.validate()

        # Report the erros using Reporter module
        Reporter(self).report()

        return self.failures

    def check_file(self, source: AnyStr, base_url: Optional[AnyStr] = None) -> None:
        # Raises an error if the file is not found.
        # This is specific to user provided file paths and not self-discovered ones
        # if not path.isfile(self.source):
        #    raise FileNotFoundError(f"File does not exist: {self.source}")
        # Invoked in case of one file check otherwise set at global by the check_directories method
        if not base_url:
            # If base URL is not provided and a single filename is provided, raise an error if the file is not found
            if not path.isfile(source):
                raise FileNotFoundError(f"File does not exist: {source}")
            # Used for internal file paths
            self.base_url = path.dirname(path.abspath(source))

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
            # Convert relative path to absolute path
            self.base_url = path.abspath(directory)
            self.LOGGER.debug(f"Base URL: {self.base_url}")

            self.LOGGER.debug(f"Crawling Directory {directory}")
            files.extend(crawl_directory(self.base_url))
            self.LOGGER.debug(f"Found {len(files)} files")

            # Remove duplicate files
            self.LOGGER.debug("Removing duplicate files")
            files = list(set(files))
            for file in files:
                self.check_file(file, self.base_url)

    def check_link(self, link: AnyStr) -> None:
        self.LOGGER.debug(f"Checking link: {link}")
        if link in self.options["ignore_urls"]:
            self.LOGGER.info(f"Ignoring link: {link}")
        # elif link in self.failures.values(): #TODO: To be fixed. failures.values returns a list of lists
        #    self.LOGGER.debug(f"Link check already failed: {link}")
        else:
            self.LOGGER.debug(f"Validating link: {link}")
            if External(link, LOGGER=self.LOGGER, options=self.options).validate():
                self.LOGGER.info(f"Found link: {link}")
            else:
                self.insert_failure(link, ["External URL"])

    def validate(self) -> None:
        self.validate_external_urls()
        self.validate_internal_urls()

    def validate_external_urls(self) -> None:
        if self.options["disable_external"]:
            self.LOGGER.info("External URL check disabled: Skipping")
            return

        for url, sources in self.external_urls.items():
            if url in self.options["ignore_urls"]:
                self.LOGGER.info("Ignoring URL: %s", url)
            # elif url in self.failures.values(): #TODO: To be fixed. failures.values returns a list of lists
            #    self.LOGGER.debug("URL check already failed: %s", url)
            else:
                self.LOGGER.debug("Validating URL: %s", url)
                if External(url, LOGGER=self.LOGGER, options=self.options).validate():
                    self.LOGGER.info(f"Found URL: {url}")
                else:
                    self.insert_failure(url, sources)

    def validate_internal_urls(self) -> None:
        for url, sources in self.internal_urls.items():
            self.LOGGER.debug(f"Checking internal URL: {url}")
            if url in self.options["ignore_urls"]:
                self.LOGGER.info(f"Ignoring URL: {url}")
            elif url in self.failures.values():
                self.LOGGER.debug(f"URL check already failed: {url}")
            else:
                self.LOGGER.debug(f"Validating URL: {url}")
                if Internal(
                    url,
                    LOGGER=self.LOGGER,
                    options=self.options,
                    base_url=self.base_url,
                ).validate():
                    self.LOGGER.info(f"Found URL: {url}")
                else:
                    self.insert_failure(url, sources)

    def get_urls(self) -> Dict[AnyStr, List]:
        return self.external_urls, self.internal_urls

    def get_failures(self) -> List:
        return self.failures

    def insert_failure(self, url: AnyStr, sources: List) -> None:
        self.LOGGER.error(f"URL missing: {url}  Sources: {sources}")
        for source in sources:
            if source in self.failures.keys():
                self.failures[source].append(url)
            else:
                self.failures[source] = [url]
