from typing import Dict


from typing import Dict


def merge_urls(urls: Dict, new_urls: Dict) -> Dict:
    for url in new_urls:
        if url in urls:
            urls[url] += new_urls[url]
        else:
            urls[url] = new_urls[url]
    return urls
