import sys
sys.path.append("../src")
from math_demo import add, add_with_bug, calculate_tax_bugged, calculate_tax

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("TEST ADDITION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0


    print("TEST BUGGED ADDITION PASSED")

def test_addition_dublicate():
    assert add(6, 7) == 6 + 7
    print("TEST DUBLICATE ADDITION PASSED")

def test_tax_calculator_pesticide():
    assert calculate_tax_bugged(1000) == 150
    assert calculate_tax_bugged(100) == 15
    assert calculate_tax_bugged(10) == 1.5
    assert calculate_tax_bugged(1) == 0.15
    assert calculate_tax_bugged(234) == 35.1
    print("TEST TAX CALCULATOR PASSED")
    # float may give us test cases
    #assert calculate_tax_bugged(2.34) == 0.35

def test_tax_calculator():
    assert calculate_tax(1000) == 150
    assert calculate_tax(100) == 15
    assert calculate_tax(10) == 1.5
    assert calculate_tax(1) == 0.15
    assert calculate_tax(234) == 35.1
    assert calculate_tax(2.34) == 0.35
    print("TEST TAX CALCULATOR PASSED")


if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicate()
    test_tax_calculator_pesticide()
    test_tax_calculator()