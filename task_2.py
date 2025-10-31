import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min < 1 or max > 1000 or max < min:
        return []
    
    if quantity < 1 or (max - min + 1) < quantity:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

# test

# print(get_numbers_ticket( 1,   49,  6))   
# print(get_numbers_ticket( 1,   36,  5))   
# print(get_numbers_ticket(10,   19, 10)) # [10...19] 
# print(get_numbers_ticket(42,   42,  1)) # [42] 
# print(get_numbers_ticket( 1, 1000,  5)) # 
# print(get_numbers_ticket(10,   19, 11)) # [] quantity
# print(get_numbers_ticket(10,   19,  0)) # [] quantity
# print(get_numbers_ticket( 0, 1000,  5)) # [] min
# print(get_numbers_ticket( 1, 1001,  5)) # [] max
