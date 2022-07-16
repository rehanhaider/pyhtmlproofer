from typing import Dict


from typing import Dict


def merge_urls(urls: Dict, new_urls: Dict) -> Dict:

    if new_urls:
        for new_url, new_source in new_urls.items():
            if new_url in urls.keys():
                urls[new_url].append(new_source)
            else:
                urls[new_url] = [new_source]
    return urls
