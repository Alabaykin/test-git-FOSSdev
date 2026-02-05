def sum(a, b):
    return a + b

def devide(a, b):
    if b  == 0:
        raise ValueError("Determinator could not be zero")
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Could not divide strings")
    return a / b

