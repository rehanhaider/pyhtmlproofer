import requests
from bs4 import BeautifulSoup


class External:
    """
    This class is used to validate external URLs.
    methods: validate -> This method is used to validate external URLs.
    """

    def __init__(self, url):
        self.url = url

    def validate(self):  # sourcery skip: assign-if-exp, boolean-if-exp-identity
        """
        This method is used to validate external URLs.
        """

        try:
            response = requests.get(self.url)
            if response.status_code != 200:  # TODO: Add more status codes including 0, 200-299, etc.
                return False
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.find("title"):
                return True
            else:
                return False
        except Exception:
            return False
