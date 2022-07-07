from pyHTMLProofer.Config import Config
from pyHTMLProofer.Utils.Log import Log


class Runner:
    def __init__(self, source, options=None):
        self.source = source
        self.options = Config.generate_defaults(options)
        self.LOGGER = Log(log_level=options["log_level"]).LOGGER

        self.external_urls = ()
        self.internal_urls = ()
        self.failures = ()

        self.before_request = ()

        self.checked_paths = ()

        self.current_check = None
        self.current_source = None
        self.current_filename = None
