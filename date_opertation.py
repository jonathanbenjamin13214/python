from datetime import date , time , datetime
today = date.today()
now = datetime.now()
current_date = now.strftime("%d/%m/%y")
current_time = now.strftime("%H:%M")
print(f"Today's date is {current_date}")
print(f"\nthe time is {current_time}")