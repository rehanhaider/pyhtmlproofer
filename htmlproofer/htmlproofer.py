"""
# --*-- coding: utf-8 --*--
# htmlproofer - A tool for validating internal & external links in HTML files / Websites
"""
from argparse import ArgumentError
import os


class HTMLProofer:
    """
    A tool for validating internal & external links in HTML files / Websites
    """

    def check_file(self, file_path):
        """
        Check the file for internal & external links
        :param file_path:
        :return:
        """
        # Raise error if file path is not a string
        if not isinstance(file_path, str):
            raise ArgumentError("File path must be a string")

        # Raise error if the file does not exist
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        print("Checking a single file")
        return True

    def check_directory(self, directory_path):
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

        print("Checking a single directory")
        return True

    def check_directories(self, directory_paths):
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

        print("Checking list of directories")
        return True

    def check_links(self, links):
        """
        Check the links for internal & external links
        :param links:
        :return:
        """

        # Raise error if link is not a string
        if not isinstance(links, list):
            raise ArgumentError("Links must be a list")

        print("Checking list of Links")
        return True
