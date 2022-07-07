from pyHTMLProofer.Version import __version__


class Config:
    """
    Configure the HTML Proofer.
    """

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
        "log_level": "INFO",
        "only_4xx": False,
        "swap_attributes": {},
        "swap_urls": {},
    }

    HTTP_DEFAULTS = {
        "followlocation": True,
        "headers": {
            "User-Agent": f"Mozilla/5.0 (compatible; HTML Proofer/{__version__}; https://github.com/rehanhaider/htmlproofer)",
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

    def generate_defaults(opts=None):
        # sourcery skip: instance-method-first-arg-name
        if opts is None:
            opts = {}

        options = Config.PROOFER_DEFAULTS.copy()  # .update(opts)
        options.update(opts)

        options["HTTP"] = dict(Config.HTTP_DEFAULTS, **options["HTTP"]) if "HTTP" in options else Config.HTTP_DEFAULTS
        options["AIOHTTP"] = (
            dict(Config.AIOHTTP_DEFAULTS, **options["AIOHTTP"]) if "AIOHTTP" in options else Config.AIOHTTP_DEFAULTS
        )
        options["PARALLEL"] = (
            dict(Config.PARALLEL_DEFAULTS, **options["PARALLEL"])
            if "PARALLEL" in options
            else Config.PARALLEL_DEFAULTS
        )
        options["CACHE"] = (
            dict(Config.CACHE_DEFAULTS, **options["CACHE"]) if "CACHE" in options else Config.CACHE_DEFAULTS
        )

        return options
