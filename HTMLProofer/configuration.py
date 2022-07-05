import HTMLProofer


class Configuration:
    DEFAULT_TESTS = ["Links", "Images", "Scripts"]

    PROOFER_DEFAULTS = {
        "allow_hash_href": True,
        "allow_missing_href": False,
        "assume_extension": ".html",
        "check_external_hash": True,
        "checks": DEFAULT_TESTS,
        "directory_index_file": "index.html",
        "disable_external": False,
        "ignore_empty_mailto": False,
        "ignore_files": [],
        "ignore_missing_alt": False,
        "ignore_status_codes": [],
        "ignore_urls": [],
        "enforce_https": True,
        "extensions": [".html"],
        "log_level": ":info",
        "only_4xx": False,
        "swap_attributes": {},
        "swap_urls": {},
    }

    HTTP_DEFAULTS = {
        "followlocation": True,
        "headers": {
            "User-Agent": f"Mozilla/5.0 (compatible; HTML Proofer/{HTMLProofer.version}; https://github.com/rehanhaider/htmlproofer)",
            "Accept": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        },
        "connecttimeout": 10,
        "timeout": 10,
    }

    AIOHTTP_DEFAULTS = {
        "max_concurrency": 50,
    }

    PARALLEL_DEFAULTS = {"enabled": True}

    CACHE_DEFAULTS = {}

    def generate_defaults(self, opts):
        """
        Generate default configuration options
        :param opts:
        :return:
        """
        options = self.PROOFER_DEFAULTS.update(opts)

        options["HTTP"] = self.HTTP_DEFAULTS.update(opts["HTTP"]) if "HTTP" in opts else self.HTTP_DEFAULTS
        options["AIOHTTP"] = (
            self.AIOHTTP_DEFAULTS.update(opts["AIOHTTP"]) if "AIOHTTP" in opts else self.AIOHTTP_DEFAULTS
        )
        options["PARALLEL"] = (
            self.PARALLEL_DEFAULTS.update(opts["PARALLEL"]) if "PARALLEL" in opts else self.PARALLEL_DEFAULTS
        )
        options["CACHE"] = self.CACHE_DEFAULTS.update(opts["CACHE"]) if "CACHE" in opts else self.CACHE_DEFAULTS
