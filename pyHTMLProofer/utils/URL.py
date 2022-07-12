"""This class validates URLs format and segregates them into internal and external URLs."""
import requests
from bs4 import BeautifulSoup


class _URL:
    def __init__(self, url, options=None):
        self.url = url
        self.options = options
        self.type = self._get_type()
        self.html_soup = None

    def validate(self):
        """
        This method is used to validate URLs.
        """

        if self.type == "external":
            return self._validate_external_url()

    def _validate_external_url(self):
        """
        This method is used to validate external URLs.
        """
        try:
            response = requests.get(
                self.url,
                headers=self.options["HTTP"]["headers"],
                timeout=self.options["HTTP"]["timeout"],
                allow_redirects=self.options["HTTP"]["followlocation"],
            )
            if response.status_code != 200:
                return False
            self.html_soup = BeautifulSoup(response.text, "html5lib")
            return True
        except Exception:
            return False

    def _validate_internal_url(self):
        """
        This method is used to validate internal URLs.
        """
        pass

    def _get_type(self):
        """
        This method is used to get the type of URL.
        """
        return "external" if self.url.startswith("http") else "internal"
