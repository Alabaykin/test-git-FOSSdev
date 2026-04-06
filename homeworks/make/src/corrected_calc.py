def add(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Arguments must to be integer")
    return a + b

try:
    result = add(2, "3")
except TypeError as e:
    print(f"Error: {e}")