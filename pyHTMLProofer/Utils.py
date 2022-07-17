from typing import Dict, Optional


def merge_urls(urls: Dict, new_urls: Dict) -> Dict:

    if new_urls:
        for new_url, new_source in new_urls.items():

            if new_url in urls.keys():
                urls[new_url].append(new_source)
            else:
                urls[new_url] = new_source
    return urls


def crawl_directory(directory: str, options: Optional[Dict] = None) -> Dict:
    """
    Crawl a directory and return a dictionary of all the HTML files found.
    """
    import glob
    from os import path

    if not isinstance(directory, str):
        raise TypeError("Input is not a directory")

    return list(glob.glob(f"{directory}/**/*.html", recursive=True))
