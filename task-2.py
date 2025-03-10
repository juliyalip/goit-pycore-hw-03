import random

def get_numbers_ticket(min, max, quantity):

    range_for_quantity = max - min
    validate = min > 1 and max < 1000 and  quantity <= range_for_quantity
    if not validate:
        return []
    
    all_numbers = range(min, max ) 
    selected_numbers = random.sample(all_numbers, quantity)
   
    return sorted(selected_numbers)