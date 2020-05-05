"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_list = {}

for call_number in calls:
    telephone_list[call_number[0]] = int(call_number[3])

key, value = max(telephone_list.items(), key=lambda x: x[1])

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(key, value))
