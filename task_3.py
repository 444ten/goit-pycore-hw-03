import re

def normalize_phone(phone_number: str) -> str:    
    res = re.sub(r'(?!^\+)\D', '', phone_number)
    
    if not res.startswith('+'):
        res = '+' + res if res.startswith('380') else '+38' + res
    
    return res


# test

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     " ..//tt ++++ 38050 111 +++ 22 +++ 11 +-+-  ",
#     "  38050 111  ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

# print("Нормалізовані номери телефонів для SMS-розсилки:")
# for _ in sanitized_numbers:
#     print(_)