"""
`pyHTMLProofer`: A tool for validating internal & external links in HTML files / Websites
"""

import os
from argparse import ArgumentError
from pyHTMLProofer.Runner import Runner


def check_file(file_path, options=None):
    """
    Check the file for internal & external links
    """
    # Raise error if file path is not a string
    if not isinstance(file_path, str):
        raise ArgumentError("File path must be a string")

    # Raise error if the file does not exist
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File does not exist: {file_path}")

    return True


def check_directory(directory_path, options=None):
    """
    Check the directory for internal & external links
    :param directory_path:
    :return:
    """

    # Raise error if directory path is not a string
    if not isinstance(directory_path, str):
        raise ArgumentError("Directory path must be a string")

    # Raise error if the directory does not exist
    if not os.path.isdir(directory_path):
        raise FileNotFoundError(f"Directory does not exist: {directory_path}")

    return True


def check_directories(directory_paths, options=None):
    """
    Check the directories for internal & external links
    :param directory_paths:
    :return:
    """

    # Raise error if directory path is not a string
    if not isinstance(directory_paths, list):
        raise ArgumentError("Directory paths must be a list")

    # Raise error if the directory does not exist
    for directory_path in directory_paths:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory does not exist: {directory_path}")

    return True


def check_links(links, options=None):
    """
    Check the links for internal & external links
    :param links:
    :return:
    """

    # Raise error if link is not a string
    if not isinstance(links, list):
        raise ArgumentError("Links must be a list")

    return True


def check_sitemap(sitemap_url, options=None):
    """
    ## Check the sitemap for internal & external links
    param: sitemap_url
    return
    """
    # Raise error if sitemap url is not a string
    if not isinstance(sitemap_url, str):
        raise ArgumentError("Sitemap url must be a string")

    print(f"Checking sitemap: {sitemap_url}")

    Runner(sitemap_url, options)
