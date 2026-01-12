from datetime import datetime, date
now = datetime.now()
print (now)
print (now.strftime("%d"))
print (now.strftime("%B"))
print (now.strftime("%Y"))
print (now.strftime("%H"))
print (now.strftime("%M"))
print (now.timestamp())
print (now.strftime("%m/%d/%Y, %H:%M:%S"))
s = "5 December, 2019"
print (datetime.strptime(s, "%d %B, %Y"))

today = date (year = 2026, day = 12, month= 1)
new_year = date (year = 2027, day= 1, month = 1)
time_left_for_newyear = new_year - today
print (time_left_for_newyear)

random_time = date (year = 1970, day = 1, month = 1)
time_spent = today - random_time
print (time_spent)