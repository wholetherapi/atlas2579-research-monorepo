from src.graph import build_adjacency


def test_empty():
    assert build_adjacency([]) == []
