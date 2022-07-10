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

    options["type"] = "file"

    return Runner(file_path, options)


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

    options["type"] = "directory"

    return Runner(directory_path, options)


def check_directories(directories, options=None):
    """
    Check the directories for internal & external links
    :param directory_paths:
    :return:
    """

    # Raise error if directory path is not a string
    if not isinstance(directories, list):
        raise ArgumentError("Directory paths must be a list")

    # Raise error if the directory does not exist
    for directory in directories:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"Directory does not exist: {directory}")

    options["type"] = "directories"

    return Runner(directories, options)


def check_links(links, options=None):
    """
    Check the links for internal & external links
    :param links:
    :return:
    """

    # Raise error if link is not a string
    if not isinstance(links, list):
        raise ArgumentError("Links must be a list")

    options["type"] = "links"

    return Runner(links, options)


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
    options["type"] = "sitemap"

    return Runner(sitemap_url, options)
