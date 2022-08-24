import pyhtmlproofer

# Disable write to file
def main():
    options = {"report_to_file": False}
    file_path = ["tests/cases/"]

    pyhtmlproofer.directories(file_path, options=options).check()
