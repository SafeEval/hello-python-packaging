# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    # Pass
    assert func(3) == 4

    # Fail
    # assert func(3) == 5
