import re

def normalize_phone(phone_number: str):
    clean_number = phone_number.strip()
    pattern = r"^\+38\d{10}$"

    if re.match(pattern,  clean_number ):
        return  clean_number 

    modified_number = re.sub(r"[^+\d]", "", clean_number)

    if re.match(pattern, modified_number):
        return modified_number
    
    if not modified_number.startswith("+"):
        modified_number = "+" + modified_number
    
    if not modified_number.startswith("+38"):
        modified_number = "+38" + modified_number.lstrip("+")

    return modified_number if re.match(pattern, modified_number) else None

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalize phone numbers for sms:", sanitized_numbers)