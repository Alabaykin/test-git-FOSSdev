def calculate_ndfl(income: int | float) -> int | float:
    result: int | float = 0
    if income <= 2_400_000:
        result = income * 0.13
    else:
        result = 2400000*0.13 + (income - 2400000) * 0.15
    9_402_000 + (income - 50_000_000) * 0.22
        
    return result
