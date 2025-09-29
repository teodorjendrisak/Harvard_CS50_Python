from twttr2 import shorten

def test_shorten_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("alphabet") == "lphbt"
    assert shorten("barbeque") == "brbq"


def test_shorten_upper():
    assert shorten("BARBEQUE") == "BRBQ"
    assert shorten("UNIQUE") == "NQ"