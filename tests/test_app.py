import pyHTMLProofer


# pyHTMLProofer.check_file("tests/out/test_dir1/test_file1.html")
# pyHTMLProofer.check_directory("tests/out")
# pyHTMLProofer.check_directories(["tests/out/test_dir1", "tests/out/test_dir2"])
# pyHTMLProofer.check_links(["https://www.google.com", "https://www.google.com/"])
pyHTMLProofer.check_sitemap("https://cloudbytes.dev/sitemap.xml", options={"log_level": "ERROR"})
