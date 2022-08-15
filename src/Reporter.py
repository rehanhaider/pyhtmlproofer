from __future__ import annotations
from tabnanny import check
from typing import TYPE_CHECKING

from rich.console import Console
from typing import AnyStr
import json

if TYPE_CHECKING:
    from Checker import Checker


class Reporter:
    """
    Class to report the results of Checker.failures dictionary.
    """

    def __init__(self, checker: Checker) -> None:
        self.failures = checker.failures
        self.options = checker.options
        self.console = Console()

    def report(self) -> None:
        """
        Prints the results of the Checker.failures dictionary.
        """
        self.console.print()
        self.console.print("################################################################################")
        if not self.failures:
            self.console.print("No failures found.")
            return
        else:
            fails = [failure for failures in self.failures.values() for failure in failures]
            # Print the number of failures and the files that have failures
            # add up the number elements in items()
            self.console.print(f"{len(fails)} failures found in {len(self.failures)} files.")

        # Print the files that have failures
        self.console.print("--------------------------------------------------------------------------------")
        self.console.print("\nFailures:")
        self.console.print("--------------------------------------------------------------------------------")
        for file_path, urls in self.failures.items():
            self.console.print(f"File: {file_path}:")
            for url in urls:
                self.console.print(f"   URL:  {url}")
            self.console.print("")

        # Write the report to file if the option is set
        if self.options["report_to_file"]:
            self.report_to_file(self.options["report_filename"])

    def report_to_file(self, file_path: AnyStr) -> None:
        """
        Prints the results of the Checker.failures dictionary to a file as JSON.
        """
        # Add "failures" key to the dictionary
        failures = {
            "metadata": {"date": "2020-01-01"},
            "failures": self.failures,
        }

        with open(file_path, "w") as file:
            file.write(json.dumps(failures, indent=4))
