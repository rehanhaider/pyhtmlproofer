# from src.HTMLProofer.htmlproofer import HTMLProofer
from HTMLProofer import HTMLProofer

proofer = HTMLProofer()
proofer.check_file("tests/out/test_dir1/test_file1.html")
proofer.check_directory("tests/out")
proofer.check_directories(["tests/out/test_dir1", "tests/out/test_dir2"])
proofer.check_links(["https://www.google.com", "https://www.google.com/"])


print(proofer.VERSION)
