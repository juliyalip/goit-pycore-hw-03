from datetime import datetime, timedelta

users =[  {"name": "Mango", "birthday": "1995.07.23"},
    {"name": "Kiwi", "birthday": "1984.03.15"},
    {"name": "Apple", "birthday": "2001.03.14"}]

def get_upcoming_birthdays(users):
  
    upcoming_birthdays =[]
    current_date = datetime.today().date()
    future_date = current_date + timedelta(days=7)
    
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        print("user_Birthday: ",user_birthday)

        if user_birthday.replace(year=current_date.year) < current_date:
           user_birthday = user_birthday.replace(year = current_date.year + 1)
        else:
            user_birthday = user_birthday.replace(year=current_date.year)
            if current_date <= user_birthday <= future_date:
                day_of_week = user_birthday.weekday()
                print(day_of_week)
                if day_of_week < 4:
                    holliday_user ={"name": user["name"],  "congratulation_date": user_birthday.strftime("%Y.%m.%d")}
                    upcoming_birthdays.append(holliday_user)
                else:
                    if day_of_week == 5:
                        user_birthday = user_birthday + timedelta(days=2)
                    elif day_of_week ==6:
                        user_birthday = user_birthday + timedelta(days=1)

                    holliday_user = {
                        "name": user["name"],
                        "congratulation_date": user_birthday.strftime("%Y.%m.%d") 
                    }
                    upcoming_birthdays.append(holliday_user)

       
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("All birthdays this week:", upcoming_birthdays)

