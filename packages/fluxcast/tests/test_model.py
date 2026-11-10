from src.model import FluxCastModel


def test_default_width():
    assert FluxCastModel().hidden == 64
