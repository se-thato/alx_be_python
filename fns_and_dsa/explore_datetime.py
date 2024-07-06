from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {formated_date}")
    return current_date

def calculate_future_date(current_date,days):
    future_date = current_date + timedelta(days = days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    current_date = display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current_date,days)

main()