""" Sample Python testing
"""


def func(_x):
    """Basic example test."""
    return _x + 1


def test_answer():
    """Another basic example test."""
    # Pass
    assert func(3) == 4

    # Fail
    assert func(3) == 5
