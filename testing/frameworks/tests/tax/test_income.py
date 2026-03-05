import sys
sys.path.append("../src")
from tax.income import calculate_tax

def test_icome_tax():

    assert calculate_tax(100) == 15
    print("TEST TAX PASSED")

if __name__ == "__main__":
    test_icome_tax()