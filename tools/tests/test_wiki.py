import pytest

from tools import wiki


def test_api_url_for_fandom_and_wikipedia():
    fandom = wiki.api_url("https://frieren.fandom.com/wiki/Scales_of_Obedience")
    assert fandom.startswith("https://frieren.fandom.com/api.php?action=parse&page=Scales_of_Obedience&prop=wikitext")
    assert "redirects=1" in fandom
    wp = wiki.api_url("https://en.wikipedia.org/wiki/Frieren_(character)#Plot")
    assert wp == "https://en.wikipedia.org/w/index.php?title=Frieren_%28character%29&action=raw"


def test_api_url_rejects_other_sites():
    with pytest.raises(ValueError):
        wiki.api_url("https://www.cbr.com/wiki/Nen")
    with pytest.raises(ValueError):
        wiki.api_url("https://hunterxhunter.fandom.com/Nen")


def test_clean_and_grep():
    raw = "'''Zoltraak''' was made by [[Qual|the demon Qual]].<ref>Chapter 5</ref>\nOther line\n\nNot related\nQual was sealed."
    text = wiki.clean(raw)
    assert text.startswith("Zoltraak was made by the demon Qual.")
    assert "<ref" not in text
    assert wiki.grep(text, ["sealed"], context=0) == "Qual was sealed."
    assert wiki.grep(text, ["zoltraak", "sealed"], context=0) == "Zoltraak was made by the demon Qual.\n---\nQual was sealed."
