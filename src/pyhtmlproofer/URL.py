from os import curdir
from sys import intern
from typing import AnyStr, Dict, Optional

from bs4 import BeautifulSoup

from .HTML import HTML


class URL:
    def __init__(
        self,
        url: AnyStr,
        LOGGER,
        options: Optional[Dict] = None,
        base_url: Optional[AnyStr] = None,
    ) -> None:
        self.url = url
        self.options = options
        self.base_url = base_url
        self.LOGGER = LOGGER


class External(URL):
    def __init__(
        self,
        url: AnyStr,
        LOGGER,
        options: Optional[Dict] = None,
        base_url: Optional[AnyStr] = None,
    ) -> None:
        super().__init__(url, LOGGER, options)

    def validate(self):
        # sourcery skip: assign-if-exp, boolean-if-exp-identity, reintroduce-else, remove-unnecessary-cast
        """
        This method is used to validate external URLs.
        """
        import requests

        try:
            response = requests.head(
                self.url,
                headers=self.options["HTTP"]["headers"],
                timeout=self.options["HTTP"]["timeout"],
                allow_redirects=self.options["HTTP"]["followlocation"],
            )
            if response.status_code != 200:
                return False
            return True
        except Exception:
            return False


class Internal(URL):
    def __init__(
        self,
        url: AnyStr,
        LOGGER,
        options: Optional[Dict] = None,
        base_url: Optional[AnyStr] = None,
    ) -> None:
        super().__init__(url, LOGGER, options, base_url)

    def validate(self):
        from os import path

        # Join two paths to get the absolute path
        self.LOGGER.debug(f"Base URL (Internal): {self.base_url}")
        # self.LOGGER.debug(f"Checking internal URL: {self.url}")
        internal_reference = None
        if self.url.startswith(self.base_url):
            internal_url_path = self.url.rstrip("/")
        else:
            internal_url_path = self.base_url + self.url.rstrip("/")

        result = False

        if "#" in internal_url_path:
            internal_reference = f"#{internal_url_path.split('#')[1]}"
            internal_url_path = internal_url_path.split("#")[0]
            # self.LOGGER.error(f"Here: {internal_url_path}")
            # self.LOGGER.error(f"Internal reference found: {internal_reference}")

        if path.isfile(internal_url_path):
            result = True
            if internal_reference is not None:
                result = self.check_reference(internal_url_path, internal_reference)
        elif path.isfile(f"{internal_url_path}{self.options['assume_extension']}"):
            result = True
            if internal_reference:
                result = self.check_reference(
                    f"{internal_url_path}{self.options['assume_extension']}",
                    internal_reference,
                )
        elif path.isfile(f"{internal_url_path}/{self.options['directory_index_file']}"):
            result = True
            if internal_reference:
                result = self.check_reference(
                    f"{internal_url_path}/{self.options['directory_index_file']}",
                    internal_reference,
                )
        return result

    def check_reference(self, internal_url_path, internal_reference):
        # get the soup from internal_url_path
        with open(internal_url_path, "r") as f:
            soup = BeautifulSoup(f.read(), "html5lib")

        html = HTML(soup, self.options)

        return html.check_reference(internal_reference)
