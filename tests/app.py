# from src.HTMLProofer.htmlproofer import HTMLProofer
from pyhtmlproofer import pyHTMLProofer

opts = {}

opts["HTTP"] = {"followlocation": False}
opts["AIOHTTP"] = {"max_concurrency": 10}

print(opts)

proofer = pyHTMLProofer()
proofer.check_file("tests/out/test_dir1/test_file1.html")
proofer.check_directory("tests/out")
proofer.check_directories(["tests/out/test_dir1", "tests/out/test_dir2"])
proofer.check_links(["https://www.google.com", "https://www.google.com/"])


print(pyHTMLProofer().Configuration().generate_defaults(opts=opts))
