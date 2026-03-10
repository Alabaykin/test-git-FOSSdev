"""
| Годовой доход | Ставка | Расчет налога |
| :--- | :--- | :--- |
| **До 2,4 млн руб.** | 13% | 13% от дохода |
| **2,4 – 5 млн руб.** | 15% | 312 000 + 15% с суммы превышения |
| **5 – 20 млн руб.** | 18% | 702 000 + 18% с суммы превышения |
| **20 – 50 млн руб.** | 20% | 3 402 000 + 20% с суммы превышения |
| **Свыше 50 млн руб.** | 22% | 9 402 000 + 22% с суммы превышения |
"""



def calculate_ndfl(income: int | float) -> int | float:
    result: int | float = 0
    
    # start addition taxrate
    tiers = [
        (0, 0, 0.13),
        (2_400_000, 312_000, 0.15),
        (5_000_000, 702_000, 0.18),
        (20_000_000, 3_402_000, 0.20),
        (50_000_000, 9_402_000, 0.22)
    ]
    
    for start, additions, taxrate in tiers[::-1]:
        if income > start:
            result =(income - start) * taxrate + additions
            
            return result
    
    raise RuntimeError(f'Error in tax calculation{income}')

