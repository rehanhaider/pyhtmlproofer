import pyHTMLProofer


def t_link():
    """Tests the check links function."""
    links = ["https://www.example.com"]

    pyHTMLProofer.links(links, options={"log_level": "ERROR"}).check()


t_link()
