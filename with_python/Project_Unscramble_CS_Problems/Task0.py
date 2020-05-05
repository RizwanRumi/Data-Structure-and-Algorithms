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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text_record = texts[0]
call_record = calls[-1]

print("First record of texts, " + text_record[0] + " texts " + text_record[1] + " at time " + text_record[2])
print("Last record of calls, " + call_record[0] + " calls " + call_record[1] + " at time " + call_record[2] +
      ", lasting " + call_record[3] + " seconds")

