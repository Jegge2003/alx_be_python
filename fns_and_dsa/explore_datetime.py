from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now() #Displaying current date and time
    current_date = now.strftime('%Y-%m-%d %H:%M:%S') #Formating to show in appropriate format
    print(f'Current date and time: {current_date}') #Displaying the current time and date

days_to_add = int(input('Enter the number of days to add to the current date: ')

def calculate_future_date():
    future_date = current_date + timedelta(days=days_to_add) # Adding a specified number of days to the current date
    future_date = future_date.strftime('%Y-%m-%d') #Showing it in the right format
    print(f'Future date: {future_date}')

