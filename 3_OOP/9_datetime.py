# From chapter 11
import datetime

# create a date object
xmas2022 = datetime.date(year=2022, month=12, day=25)
current_date = datetime.date.today() # get current date

print(f'Xmas 2022 = {xmas2022}')
print(f'Today = {current_date}')

print((xmas2022 - current_date).days, 'days to Christmas this year.') # print timedelta object details

# datetime.datetime example
class_end_time = datetime.datetime(year=2022, month=2, day=7, hour=11, minute=30) # create a timestamp
current_time = datetime.datetime.now() # get current datetime
print(class_end_time - current_time) # create a timedelta object