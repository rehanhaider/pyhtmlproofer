"""
# Proof HTML Files
"""
import glob
from bs4 import BeautifulSoup


class HTMLProofer:
    """
    Takes either a path or sitemap url and returns a list of all links in the HTML.
    """

    def __init__(self) -> None:
        self.links = set()
        self.images = set()
        self.scripts = set()
        self.styles = set()

    def check_directory(self, path: str) -> None:
        """
        Checks a directory for all links in the HTML.
        """
        # check for filenames ending with .html using glob.glob
        for file in glob.iglob(path + "/**/*.html", recursive=True):
            self.check_file(file)

    def check_file(self, file_path):
        """
        Checks a HTML file for all external links in the HTML.
        TODO: Add a feature to check for internal links
        """
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html5lib")
            for link in soup.find_all("a"):
                if link.get("href").startswith("http"):
                    self.links.add(link.get("href"))
            for image in soup.find_all("img"):
                if image.get("src").startswith("http"):
                    self.images.add(image.get("src"))
            for script in soup.find_all("script"):
                if script.get("src").startswith("http"):
                    self.scripts.add(script.get("src"))
            for style in soup.find_all("style"):
                if style.get("src").startswith("http"):
                    self.styles.add(style.get("src"))
