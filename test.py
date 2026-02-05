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

def rest_devide_zero():
    a = 2
    b = 0
    try:
        devide(a, b)
        assert False
    except ValueError as err:
        print("divided by zero")
