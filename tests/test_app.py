import pyHTMLProofer
from pyHTMLProofer.Version import __version__


def test_app():
    """Tests the app."""
    sitemap = "https://cloudbytes.dev/sitemap.xml"
    pyHTMLProofer.check_sitemap(sitemap, options={"log_level": "INFO"}).run()


urls = [
    "https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi",
]


headers = {
    "User-Agent": f"Mozilla/5.0 (compatible; pyHTMLProofer/{__version__})",
    "Accept": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5",
}


def some():
    import requests

    for url in urls:
        r = requests.get(url, headers=headers)
        print(r.status_code)


# some()
