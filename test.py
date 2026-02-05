from .script import sum, devide

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result
def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert divide(a, b) == result

