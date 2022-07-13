"""
`pyHTMLProofer`: A tool for validating internal & external links in HTML files / Websites
"""

import requests
from argparse import ArgumentError
from pyHTMLProofer.Runner import Runner

# Not included in first release
# def check_links(links, options=None):
#    """
#    Check the links for internal & external links
#    :param links:
#    :return:
#    """
#
#    # Raise error if link is not a string
#    if not isinstance(links, list):
#        raise ArgumentError("Links must be a list")
#
#    options["type"] = "links"
#
#    return Runner(links, options)


def check_sitemap(sitemap_url, options=None):
    """
    ## Check the sitemap for internal & external links
    param: sitemap_url
    return
    """
    # Raise error if sitemap url is not a string
    if not isinstance(sitemap_url, str):
        raise ArgumentError("Sitemap url must be a string")

    # Raise error if the sitemap does not exist
    if requests.get(sitemap_url).status_code != 200:
        raise FileNotFoundError(f"Sitemap does not exist: {sitemap_url}")

    print(f"Checking sitemap: {sitemap_url}")
    options["type"] = "sitemap"

    return Runner(sitemap_url, options)
