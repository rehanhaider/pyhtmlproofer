import logging


class Log:
    """Configure the logger with log level from the below options.
    Options: ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
    """

    def __init__(self, log_level: str = "INFO"):
        """Initialise the logger.

        Args:
            log_level (str, optional): Set the log level. Defaults to "INFO".

        Options:
            "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
        """
        DEFAULT_LEVELS = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
        if log_level not in DEFAULT_LEVELS:
            raise ValueError(f"Log level must be one of the following: {DEFAULT_LEVELS}")

        # Fix this in future
        logging.basicConfig(level=eval(f"logging.{log_level}"))
        self.LOGGER = logging.getLogger("pyHTMLProofer")
        self.LOGGER.setLevel(eval(f"logging.{log_level}"))
