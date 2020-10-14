import math

day_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

def get_day_nextmonth(year, month, day=0):
	days = get_days_of_month(year, month)
	return (days+day)%7 

def get_days_of_month(year, month):
	if month in (1,3,5,7,8,10,12) : return 31
	elif month != 2:
		return 30
	elif is_leap_year(year):
		return 29
	return 28

def is_leap_year(year):
	if year % 400  == 0 : return True
	elif year % 100 == 0 : return False
	elif year % 4 == 0 : return True
	return False

# print(get_day_nextmonth(1900, 1, 0))

monday_list = []
next_day = 0 # initially monday for Jan 1900
for year in range(1900,2001):
	for month in range(1,13):
		next_day = get_day_nextmonth(year,month,next_day)
		if next_day == 6 : monday_list.append(f"{year}.{month+1}")

print(len(monday_list))