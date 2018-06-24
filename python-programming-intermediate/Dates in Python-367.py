## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time

current_time = time.time()
current_struct_time = time.gmtime()
current_hour = current_struct_time.tm_hour

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

kirks_birthday = datetime.datetime(month=3, day=22, year=2233)
diff = datetime.timedelta(weeks=15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

import datetime

string = '%I:%M%p on %A %B %d, %Y'
mystery_date_formatted_string = mystery_date.strftime(string)

print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

f = '%I:%M%p on %A %B %d, %Y'
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, f)

print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime

for row in posts:
    row[2] = datetime.datetime.fromtimestamp(float(row[2]))

## 9. Counting Posts from March ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
def func(month):
    march_count = 0
    for row in posts:
        if row[2].month == month:
            march_count += 1
    return march_count
            
feb_count = func(2)
aug_count = func(8)