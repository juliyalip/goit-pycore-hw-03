from datetime import datetime
import re
import random

# task 1

def get_days_from_today(date):
    pattern = r"\d{4}-\d{2}-\d{2}"
    result = re.findall(pattern, date)
    if not result:
        print("Please add a correct format 'yyyy-mm-dd")
        return None
    
    specific_date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    current_date_obj =  datetime.today().date()
    
    difference = current_date_obj - specific_date_obj

    return difference
   
print(get_days_from_today( '2025-03-18'))


# task 2

def get_numbers_ticket(min, max, quantity):

    range_for_quantity = max - min
    validate = min > 1 and max < 1000 and  quantity <= range_for_quantity
    if not validate:
        return []
    
    all_numbers = range(min, max ) 
    selected_numbers = random.sample(all_numbers, quantity)
   
    return sorted(selected_numbers)
    
print(get_numbers_ticket(3, 79, 7))

  
# task 3

def normalize_phone(phone_number: str):
    clean_number = phone_number.strip()
    pattern = r"^\+380\d{9}$"

    if re.match(pattern,  clean_number ):
        return  clean_number 
    else:
        
        modified_number = re.sub(r"[^+\d]", "", clean_number)
        return modified_number

print(normalize_phone("+38(096)7894339"))
