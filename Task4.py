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

def getUniqueNumbers(tbl):
    outgoing_numbers = []
    incoming_numbers = []
    for item in tbl:
        outgoing_numbers.append(item[0])
        incoming_numbers.append(item[1])
    return list(set(outgoing_numbers)), list(set(incoming_numbers))


def getLikelyTeleMarketers():
    unique_outgoing_calls_numbers, unique_incoming_calls_numbers = getUniqueNumbers(calls)
    unique_outgoing_texts_numbers, unique_incoming_texts_numbers = getUniqueNumbers(texts)
    likely_telemarketers = []
    for number in unique_outgoing_calls_numbers:
        if (number not in unique_incoming_calls_numbers) and (number not in unique_outgoing_texts_numbers) and (number not in unique_incoming_texts_numbers):
            likely_telemarketers.append(number)
    likely_telemarketers.sort()
    return likely_telemarketers

def printLikelyTelemarketers():
    likely_telemarketers = getLikelyTeleMarketers()
    print("These numbers could be telemarketers: ")
    for number in likely_telemarketers:
        print(number)

printLikelyTelemarketers()