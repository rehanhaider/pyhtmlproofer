from typing import AnyStr, Dict, Optional
from .Checker import Checker


def file(file_path: AnyStr, options: Optional[Dict] = None) -> None:
    """
    Check a file.
    """

    # Raise error if file path is not a string
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    options["type"] = "file"

    return Checker(file_path, options=options)
