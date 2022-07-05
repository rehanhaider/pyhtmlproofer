from src.HTMLProofer.htmlproofer import HTMLProofer


def test_htmlproofer():
    proofer = HTMLProofer()
    assert proofer.check_file("tests/test_app.py") == True
