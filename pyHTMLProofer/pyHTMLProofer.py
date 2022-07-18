from typing import AnyStr, Dict, List, Optional
from .Checker import Checker


def file(file_path: AnyStr, options: Optional[Dict] = None) -> None:
    """
    Check a file.
    """

    # Raise error if file path is not a string
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")

    options["type"] = "file"

    return Checker(file_path, options=options)


def directories(directories_path: List, options: Optional[Dict] = None) -> None:
    """
    Check a directory.
    """

    # Raise error if directory path is not a string
    if not isinstance(directories_path, list):
        raise TypeError("Input must be a list of directories")

    options["type"] = "directories"

    return Checker(directories_path, options=options)


# TODO: Implement link check
