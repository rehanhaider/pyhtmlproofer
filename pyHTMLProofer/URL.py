from typing import AnyStr


class URL:
    def __init__(self, url: AnyStr, options=None) -> None:
        self.url = url
        self.options = options


class External(URL):
    def __init__(self, url: AnyStr, options=None) -> None:
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
    def __init__(self, url: AnyStr, options=None) -> None:
        super().__init__(url, options)
