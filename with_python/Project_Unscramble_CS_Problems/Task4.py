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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


telemarketers_list = set()
received_telemarketers = set()
selected_telemarketers = []
code = '140'

for callNum in calls:
    number = callNum[0]
    if number[0:3] == code:
        telemarketers_list.add(callNum[0])

for callNum in calls:
    received_telemarketers.add(callNum[1])

for textNum in texts:
    received_telemarketers.add(textNum[0])
    received_telemarketers.add(textNum[1])

for number in telemarketers_list:
    if number not in received_telemarketers:
        selected_telemarketers.append(number)

selected_telemarketers.sort()

print("These numbers could be telemarketers: ")
for number in selected_telemarketers:
    print(number)



