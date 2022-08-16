import pyHtmlProofer

# Disable write to file
def main():
    options = {"report_to_file": False}
    file_path = ["tests/cases/5/"]

    pyHtmlProofer.directories(file_path, options=options).check()
