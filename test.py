from htmlproofer import HTMLProofer


HTML = HTMLProofer()
HTML.check_directory("output")
