from .__version__ import __version__


class Config:
    """
    Configure the HTML Proofer.
    """

    DEFAULT_TESTS = ["Links", "Images", "Scripts"]

    PROOFER_DEFAULTS = {
        "assume_extension": ".html",
        "check_external_hash": False,  # TODO: implement this to check reference in external files
        "checks": DEFAULT_TESTS,  # TODO: Only links are supported at the moment. Add more tests for "Links", "Images" & "Scripts"
        "directory_index_file": "index.html",
        "disable_external": False,
        "ignore_files": [],
        "ignore_urls": [],
        "enforce_https": True,
        "extensions": [".html"],
        "log_level": "ERROR",
        "report_to_file": True,
        "report_filename": "proofer_report",
    }

    HTTP_DEFAULTS = {
        "followlocation": True,  # TODO: implement this to follow redirects
        "headers": {
            "User-Agent": f"Mozilla/5.0 (compatible; pyHTMLProofer/{__version__})",
            "Accept": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
        },
        "timeout": 10,  # TODO: implement this to set a timeout
    }

    AIOHTTP_DEFAULTS = {  # TODO: implement this for parallel requests
        "max_concurrency": 10,
    }

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

        return options
