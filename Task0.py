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

def getRecords():
    textsFirstRecord = texts[0]
    callsLastRecord = calls[-1]
    print("First record of texts, " + textsFirstRecord[0] + 
            " texts " + textsFirstRecord[1] + " at time " + textsFirstRecord[2])
    print("Last record of calls, " + callsLastRecord[0] +
            " calls " + callsLastRecord[1] + " at time " + callsLastRecord[2] +
            ", lasting " + callsLastRecord[3] + " seconds")

getRecords()
