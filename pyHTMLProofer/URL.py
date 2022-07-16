from os import curdir
from typing import AnyStr, Dict, Optional


class URL:
    def __init__(self, url: AnyStr, options: Optional[Dict] = None, base_url: Optional[AnyStr] = None) -> None:
        self.url = url
        self.options = options
        self.base_url = base_url


class External(URL):
    def __init__(self, url: AnyStr, options: Optional[Dict] = None, base_url: Optional[AnyStr] = None) -> None:
        super().__init__(url, options)

    def validate(self):
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
    def __init__(self, url: AnyStr, options: Optional[Dict] = None, base_url: Optional[AnyStr] = None) -> None:
        super().__init__(url, options, base_url)

    def validate(self):
        from os import path

        # Join two paths to get the absolute path
        internal_url_path = self.base_url + self.url
        if path.isfile(internal_url_path):
            return True
        elif path.isfile(f"{internal_url_path}{self.options['assume_extension']}"):
            return True
        elif path.isfile(f"{internal_url_path}/{self.options['directory_index_file']}"):
            return True
        else:
            return False
