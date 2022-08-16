from logging import Logger
from typing import Dict, Optional

LOGGER = Logger("pyHTMLProofer")


def merge_urls(urls: Dict, new_urls: Dict) -> Dict:
    if new_urls:
        for (
            new_url,
            new_sources,
        ) in new_urls.items():  # Structure is {url: [source1, source2]}
            if new_url in urls.keys():
                for new_source in new_sources:  # Iterate over the values list - new_sources
                    urls[new_url].append(new_source)
            else:
                urls[new_url] = new_sources
    return urls


def crawl_directory(directory: str, options: Optional[Dict] = None) -> Dict:
    """
    Crawl a directory and return a dictionary of all the HTML files found.
    """
    import glob
    from os import path

    # raise an error if the directory doesn't exist
    if not path.exists(directory):
        raise FileNotFoundError(f"Directory {directory} does not exist")

    # if not isinstance(directory, str):
    #    raise TypeError("Input is not a directory")

    return list(glob.glob(f"{directory}/**/*.html", recursive=True))
