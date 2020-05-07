"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
telephone_list = []

for text_number in texts:
    telephone_list.append(text_number[0])
    telephone_list.append(text_number[1])

for call_number in calls:
    telephone_list.append(call_number[0])
    telephone_list.append(call_number[1])

unique_numbers = set(telephone_list)

print("There are {0} different telephone numbers in the records.".format(len(unique_numbers)))

'''

unique_numbers = set()

for textNumber in texts:
    unique_numbers.add(textNumber[0])
    unique_numbers.add(textNumber[1])

for callNumber in calls:
    unique_numbers.add(callNumber[0])
    unique_numbers.add(callNumber[1])

print("There are {0} different telephone numbers in the records.".format(len(unique_numbers)))
