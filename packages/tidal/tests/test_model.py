from src.model import TidalEnsemble


def test_members():
    assert TidalEnsemble().members == 8
