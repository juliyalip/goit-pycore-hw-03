from datetime import datetime
import re

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
   





